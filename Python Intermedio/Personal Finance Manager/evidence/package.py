"""
Student: Cesar Lanuza Urbina
Program: Package the finance project source, instructions, tests, and verification evidence.
"""

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


def main():
    """Exclude environments, caches, and personal data from the delivery archive."""
    root = Path(__file__).resolve().parents[1]
    destination = root / "Gestor_Finanzas_Personales.zip"
    excluded = {".venv", "__pycache__", ".pytest_cache", "data", ".git"}
    with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob("*")):
            relative = path.relative_to(root)
            if not path.is_file() or any(part in excluded for part in relative.parts):
                continue
            if path.suffix in {".zip", ".pyc", ".tmp"}:
                continue
            archive.write(path, str(relative))
    print(f"Delivery archive generated: {destination}")


if __name__ == "__main__":
    main()