"""Compare the finance delivery archive with current sources and test its contents."""

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from zipfile import ZipFile


PROJECT = Path(r"C:\Lyfter\Python Intermedio\Personal Finance Manager")
ARCHIVE = PROJECT / "Gestor_Finanzas_Personales.zip"
EXCLUDED = {".venv", "__pycache__", ".pytest_cache", "data", ".git"}


def main():
    """Check integrity, completeness, content hashes, guide metadata, and packaged tests."""
    expected = {
        path.relative_to(PROJECT).as_posix(): path
        for path in PROJECT.rglob("*")
        if path.is_file()
        and not any(part in EXCLUDED for part in path.relative_to(PROJECT).parts)
        and path.suffix not in {".zip", ".pyc", ".tmp"}
    }
    with ZipFile(ARCHIVE) as archive:
        assert archive.testzip() is None, "El ZIP contiene un archivo corrupto."
        names = archive.namelist()
        assert len(names) == len(set(names)), "El ZIP contiene rutas duplicadas."
        actual = {name for name in names if not name.endswith("/")}
        missing = sorted(set(expected) - actual)
        extra = sorted(actual - set(expected))
        changed = sorted(name for name in actual & set(expected)
                         if archive.read(name) != expected[name].read_bytes())
        print(json.dumps({"faltantes": missing, "adicionales": extra, "diferentes": changed},
                         ensure_ascii=False, indent=2), flush=True)
        if missing or extra or changed:
            raise SystemExit(1)
        print(f"Integridad y contenido correctos: {len(actual)} archivos idénticos al proyecto.", flush=True)
        review = json.loads(archive.read("evidence/user_guide_review.json"))
        guide = archive.read("documentation/Guia_del_Usuario_Gestor_Finanzas.pdf")
        assert hashlib.sha256(guide).hexdigest() == review["sha256"]
        assert review["pages"] == 11 and review["updated_on"] == "2026-10-23"
        assert "tests/test_transaction_changes.py" in actual
        print("Guía de 11 páginas verificada mediante SHA-256; pruebas de edición y eliminación incluidas.", flush=True)
        if "--test" in sys.argv:
            with tempfile.TemporaryDirectory(prefix="finance-archive-") as temporary:
                for name in actual:
                    target = Path(temporary, name).resolve()
                    assert target.is_relative_to(Path(temporary).resolve())
                archive.extractall(temporary)
                result = subprocess.run([sys.executable, "-m", "pytest", "-q"], cwd=temporary)
                assert result.returncode == 0, "Fallaron las pruebas del contenido extraído."
                print("Pruebas ejecutadas desde el ZIP extraído en una carpeta temporal.", flush=True)
                result = subprocess.run([sys.executable, "verify_interface.py"], cwd=temporary)
                assert result.returncode == 0, "Falló la integración gráfica del contenido extraído."
                print("Integración gráfica verificada desde el ZIP con datos temporales.", flush=True)
    print(f"SHA-256 del ZIP: {hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()}", flush=True)


if __name__ == "__main__":
    main()
