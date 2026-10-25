"""
Student: Cesar Lanuza Urbina
Program: Show a real application validation message for the user guide screenshot.
"""
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Lyfter\Python Intermedio\Gestor de Finanzas Personales")
from gestor_finanzas.errores import ErrorFinanzas
from gestor_finanzas.interfaz import configure_theme, show_error
from gestor_finanzas.logica import GestorFinanzas
from gestor_finanzas.persistencia import RepositorioFinanzas


def main():
    """Trigger domain validation before any state can be modified."""
    configure_theme()
    manager = GestorFinanzas(RepositorioFinanzas(Path(__file__).parent / "demo" / "finanzas.json"))
    try:
        manager.record_transaction("Compra", "1", None, "Gasto", "22/10/2026")
    except ErrorFinanzas as error:
        show_error(error)


if __name__ == "__main__":
    main()