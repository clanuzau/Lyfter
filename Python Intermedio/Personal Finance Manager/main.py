"""
Student: Cesar Lanuza Urbina
Program: Start the personal finance desktop application with protected local storage.
"""

import os
import sys
from pathlib import Path

from finance_manager.errors import FinanceError
from finance_manager.logic import FinanceManager
from finance_manager.persistence import FinanceRepository

PROJECT_DIR = Path(__file__).resolve().parent


class SingleInstanceLock:
    """Prevent two application instances from overwriting the same data file."""

    # The lock file is created in the same folder as the data file, with a .lock extension.
    def __init__(self, path):
        """Configure a lock next to the data file."""
        self.path = Path(path)
        self.file = None

    # Acquire a nonblocking OS lock released automatically on process exit.
    def __enter__(self):
        """Acquire a nonblocking OS lock released automatically on process exit."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.file = self.path.open("a+b")
        try:
            if os.name == "nt":
                import msvcrt
                self.file.seek(0, os.SEEK_END)
                if self.file.tell() == 0:
                    self.file.write(b"0")
                    self.file.flush()
                self.file.seek(0)
                msvcrt.locking(self.file.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            self.file.close()
            self.file = None
            raise FinanceError("El gestor ya está abierto con este archivo de datos. Cierre la otra ventana e inténtelo de nuevo.")
        return self

    # Release the lock handle even if initialization or the GUI fails.
    def __exit__(self, *exc):
        """Close the lock handle even if initialization or the GUI fails."""
        if self.file is not None:
            self.file.close()


def main():
    """Load saved records before starting FreeSimpleGUI and show Spanish errors."""
    try:
        from finance_manager.controller import FinanceController
        from finance_manager.interface import FinanceApplication, show_error
    except ImportError:
        print("Faltan dependencias. Ejecute setup.bat y luego start.bat desde la carpeta del proyecto.")
        return 1
    data_path = Path(os.environ.get("GESTOR_FINANZAS_DATA", PROJECT_DIR / "data" / "finanzas.json")).resolve()
    try:
        with SingleInstanceLock(data_path.with_suffix(".lock")):
            repository = FinanceRepository(data_path)
            app = FinanceApplication(FinanceController(FinanceManager(repository)))
            app.run()
        return 0
    except FinanceError as error:
        show_error(error)
        return 1
    except OSError:
        show_error("No se pudo acceder a la carpeta de datos. Revise los permisos antes de iniciar.")
        return 1


if __name__ == "__main__":
    sys.exit(main())