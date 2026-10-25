"""
Student: Cesar Lanuza Urbina
Program: Verify real FreeSimpleGUI windows and complete application workflows with isolated temporary data.
"""

import csv
import tempfile
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch

from finance_manager import interface as ui
from finance_manager.controller import FinanceController
from finance_manager.logic import FinanceManager
from finance_manager.persistence import FinanceRepository


def run_verification():
    """Exercise actual Tk widgets and event handlers without changing user data."""
    results = []
    errors = []
    today = date.today().strftime("%d/%m/%Y")
    yesterday = (date.today() - timedelta(days=1)).strftime("%d/%m/%Y")
    tomorrow = (date.today() + timedelta(days=1)).strftime("%d/%m/%Y")
    with tempfile.TemporaryDirectory(prefix="gestor-verificacion-") as temporary:
        repository = FinanceRepository(Path(temporary) / "finanzas.json")
        manager = FinanceManager(repository)
        controller = FinanceController(manager)
        app = ui.FinanceApplication(controller, hidden=True)
        category_factory = ui.create_category_window
        movement_factory = ui.create_transaction_window

        def category_form(category=None):
            """Fill and submit the same category window used by the application."""
            window = category_factory(category, hidden=True)
            def submit():
                window["-NAME-"].update("Alimentación" if category is None else "Comida")
                window["-COLOR-"].update("#DCEEF8" if category is None else "#001122")
                window.write_event_value("-SAVE-", None)
            window.TKroot.after(60, submit)
            return window

        def movement_form(kind, categories):
            """Fill and submit actual income and expense forms."""
            window = movement_factory(kind, categories, hidden=True)
            def submit():
                window["-TITLE-"].update("Salario" if kind == "Ingreso" else "Café")
                window["-AMOUNT-"].update("1000,50" if kind == "Ingreso" else "200.25")
                window["-CATEGORY-"].update(categories[0].nombre)
                window["-DATE-"].update(yesterday if kind == "Ingreso" else today)
                window.write_event_value("-SAVE-", None)
            window.TKroot.after(60, submit)
            return window

        try:
            assert app.window["-TABLE-"].Values == []
            results.append("Inicio vacío y tabla operativa")
            with patch.object(ui, 'show_error', side_effect=lambda message: errors.append(str(message))):
                app.handle_event("-ADD-EXPENSE-", {})
            assert "crear una categoría" in errors[-1]
            results.append("Movimiento sin categorías bloqueado")

            with patch.object(ui, 'create_category_window', side_effect=category_form):
                app.handle_event("-ADD-CATEGORY-", {})
            assert len(manager.categories) == 1
            results.append("Categoría creada desde su ventana")

            with patch.object(ui, 'create_transaction_window', side_effect=movement_form):
                app.handle_event("-ADD-INCOME-", {})
                app.handle_event("-ADD-EXPENSE-", {})
            assert len(app.window["-TABLE-"].Values) == 2
            assert controller.get_view().balance == "₡ 800,25"
            results.append("Ingreso y gasto registrados desde ventanas separadas")

            with patch.object(ui, 'create_category_window', side_effect=category_form):
                app.handle_event("-EDIT-CATEGORY-", {"-EDIT-SELECTION-": "Alimentación"})
            assert all(color[2] == "#001122" for color in controller.get_view().colores)
            tree = app.window["-TABLE-"].Widget
            for item in tree.get_children():
                tags = tree.item(item, "tags")
                assert any(str(tree.tag_configure(tag, "background")).upper() == "#001122" for tag in tags)
            results.append("Nombre y color editados y aplicados a las filas reales")

            app.handle_event("-FILTER-", {"-START-": today, "-END-": today})
            assert len(app.window["-TABLE-"].Values) == 1
            assert controller.get_view().balance == "₡ -200,25"
            results.append("Filtro inclusivo y totales visibles actualizados")

            before = manager.transactions
            with patch.object(ui, 'show_error', side_effect=lambda message: errors.append(str(message))):
                app.handle_event("-FILTER-", {"-START-": today, "-END-": yesterday})
            assert len(app.window["-TABLE-"].Values) == 1
            try:
                controller.save_transaction({"-TITLE-": "Futuro", "-AMOUNT-": "1", "-DATE-": tomorrow},
                                             "Gasto", manager.categories[0].id)
            except ui.FinanceError as error:
                assert "futura" in str(error)
            else:
                raise AssertionError("Se aceptó una fecha futura.")
            assert manager.transactions == before
            results.append("Rango inválido y fecha futura rechazados sin cambios")

            destination = Path(temporary) / "reporte.csv"
            with patch.object(ui.sg, "popup_get_file", return_value=str(destination)):
                app.handle_event("-EXPORT-", {})
            with destination.open(encoding="utf-8-sig", newline="") as file:
                rows = list(csv.reader(file))
            assert len(rows) == 7
            assert rows[-1][2] == "800.25"
            results.append("CSV completo con signos y totales pese al filtro activo")

            app.handle_event("-CLEAR-FILTER-", {})
            assert len(app.window["-TABLE-"].Values) == 2
            restored = FinanceManager(FinanceRepository(repository.path))
            assert restored.categories == manager.categories
            assert restored.transactions == manager.transactions
            results.append("Filtro quitado y persistencia comprobada tras recarga")

            # Save a clearly labeled sample only when this verification succeeds.
            sample_path = Path(__file__).resolve().parent / "evidence" / "sample_export.csv"
            controller.export(sample_path)

            def edit_movement_form(kind, categories, transaction):
                """Check actual prefilled widgets and save an edited transaction."""
                window = movement_factory(kind, categories, hidden=True, transaction=transaction)
                assert window["-TITLE-"].get() == transaction.titulo
                assert window["-AMOUNT-"].get() == str(transaction.monto)
                assert window["-DATE-"].get() == transaction.fecha.strftime("%d/%m/%Y")
                assert window["-KIND-"].get() == transaction.tipo
                assert window["-CATEGORY-"].get() == "Comida"

                def submit():
                    window["-TITLE-"].update("Movimiento editado")
                    window["-AMOUNT-"].update("50,00")
                    window["-KIND-"].update("Ingreso")
                    window["-DATE-"].update(yesterday)
                    window.write_event_value("-SAVE-", None)

                window.TKroot.after(60, submit)
                return window

            app.handle_event("-FILTER-", {"-START-": today, "-END-": today})
            selected_id = app._transaction_ids[0]
            with patch.object(ui, "create_transaction_window", side_effect=edit_movement_form):
                app.handle_event("-EDIT-TRANSACTION-", {"-TABLE-": [0]})
            assert app.window["-TABLE-"].Values == []
            assert controller.get_view().balance == "₡ 0,00"
            updated = manager.get_transaction(selected_id)
            assert updated.titulo == "Movimiento editado" and updated.tipo == "Ingreso"
            assert FinanceManager(FinanceRepository(repository.path)).get_transaction(selected_id) == updated
            results.append("Edición con campos precargados, cambio de tipo y fecha, guardado y filtro actualizado")

            app.handle_event("-CLEAR-FILTER-", {})
            index = app._transaction_ids.index(selected_id)
            before = repository.path.read_bytes()
            with patch.object(ui.sg, "popup", autospec=True, return_value="Cancelar"):
                app.handle_event("-DELETE-TRANSACTION-", {"-TABLE-": [index]})
            assert repository.path.read_bytes() == before
            with patch.object(ui.sg, "popup", autospec=True, return_value="Confirmar"):
                app.handle_event("-DELETE-TRANSACTION-", {"-TABLE-": [index]})
            assert len(app.window["-TABLE-"].Values) == 1
            assert controller.get_view().balance == "₡ 1.000,50"
            assert FinanceManager(FinanceRepository(repository.path)).transactions == manager.transactions
            results.append("Eliminación cancelada y confirmada, tabla y totales actualizados, recarga sin el registro")
        finally:
            app.window.close()
    return results


if __name__ == "__main__":
    try:
        for item in run_verification():
            print(f"EXITOSO: {item}.")
    except Exception:
        print("FALLIDO: no se completó la verificación de interfaz. Revise el detalle técnico de la ejecución.")
        raise
