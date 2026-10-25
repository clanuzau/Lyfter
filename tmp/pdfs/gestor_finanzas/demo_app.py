"""
Student: Cesar Lanuza Urbina
Program: Display the finance application with fictional data for user guide screenshots.
"""
import sys
from pathlib import Path

PROJECT = Path(r"C:\Lyfter\Python Intermedio\Gestor de Finanzas Personales")
sys.path.insert(0, str(PROJECT))

from gestor_finanzas.controlador import ControladorFinanzas
from gestor_finanzas.interfaz import AplicacionFinanzas
from gestor_finanzas.logica import GestorFinanzas
from gestor_finanzas.persistencia import RepositorioFinanzas


def main():
    """Use a dedicated demonstration repository and leave user data untouched."""
    path = Path(__file__).resolve().parent / "demo" / "finanzas.json"
    manager = GestorFinanzas(RepositorioFinanzas(path))
    if not manager.categories:
        salary = manager.create_category("Salario", "#DDF0E8")
        food = manager.create_category("Alimentación", "#FBE8D4")
        transport = manager.create_category("Transporte", "#DDEBFA")
        services = manager.create_category("Servicios", "#EEE5F9")
        for title, amount, category, kind, day in [
            ("Salario de octubre", "950000", salary, "Ingreso", "01/10/2026"),
            ("Servicio de Internet", "25000", services, "Gasto", "05/10/2026"),
            ("Compra de supermercado", "42000", food, "Gasto", "12/10/2026"),
            ("Proyecto independiente", "125000", salary, "Ingreso", "15/10/2026"),
            ("Combustible", "18000", transport, "Gasto", "20/10/2026"),
            ("Café y almuerzo", "6500", food, "Gasto", "22/10/2026"),
        ]:
            manager.record_transaction(title, amount, category.id, kind, day)
    app = AplicacionFinanzas(ControladorFinanzas(manager))
    app.run()


if __name__ == "__main__":
    main()