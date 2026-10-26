"""
Student: Cesar Lanuza Urbina
Program: Verify the Windows setup script in a clean temporary project directory.
"""

import shutil
import subprocess
import tempfile
from pathlib import Path


def main():
    """Install from pinned requirements in isolation and verify package imports."""
    project = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="finance-installation-") as directory:
        target = Path(directory).resolve()
        # The temporary directory is created by this process and holds no user files.
        for name in ("setup.bat", "requirements.txt", "requirements-dev.txt"):
            shutil.copy2(project / name, target / name)
        result = subprocess.run(["cmd.exe", "/d", "/c", "setup.bat"], cwd=target,
                                capture_output=True, text=True, encoding="utf-8", errors="replace")
        evidence = project / "evidence" / "clean_installation.txt"
        evidence.write_text(result.stdout + result.stderr, encoding="utf-8")
        if result.returncode:
            print("FAILED: clean installation did not complete successfully. See evidence/clean_installation.txt.")
            return result.returncode
        python = target / ".venv" / "Scripts" / "python.exe"
        check = subprocess.run([str(python), "-c", "import tkinter, FreeSimpleGUI, pytest"],
                               cwd=target, capture_output=True, text=True)
        if check.returncode:
            print("FAILED: dependencies could not be imported in the new environment.")
            return check.returncode
        print("PASSED: clean installation with setup.bat and successful dependency imports.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())