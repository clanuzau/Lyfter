"""
Student: Cesar Lanuza Urbina
Program: Display Spanish FreeSimpleGUI windows and route desktop events through the controller.
"""

from datetime import date

import FreeSimpleGUI as sg

from .errors import FinanceError, ValidationError

BACKGROUND = "#F4F7FA"
PRIMARY = "#14354B"
ACCENT = "#126B61"


def configure_theme():
    """Use a readable light theme and Spanish text throughout the application."""
    sg.theme("LightGrey1")
    sg.set_options(font=("Segoe UI", 10), background_color=BACKGROUND,
                   text_element_background_color=BACKGROUND, text_color=PRIMARY,
                   button_color=("#FFFFFF", PRIMARY), element_padding=(5, 5))


def show_error(message):
    """Display a recoverable domain or file error in Spanish."""
    sg.popup(str(message), title="No se pudo completar la operación", custom_text=("Aceptar", None), keep_on_top=True)


def create_category_window(category=None, hidden=False):
    """Build a separate category form with a native color chooser."""
    editing = category is not None
    layout = [
        [sg.Text("Editar categoría" if editing else "Nueva categoría", font=("Segoe UI", 16, "bold"))],
        [sg.Text("Las categorías se comparten entre ingresos y gastos.")],
        [sg.Text("Nombre", size=(10, 1)), sg.Input(category.nombre if editing else "", key="-NAME-", size=(35, 1))],
        [sg.Text("Color", size=(10, 1)), sg.Input(category.color if editing else "#DCEEF8", key="-COLOR-", size=(15, 1)),
         sg.ColorChooserButton("Elegir color", target="-COLOR-", key="-CHOOSE-COLOR-")],
        [sg.Text("Formato de color: #RRGGBB. Ejemplo: #DCEEF8")],
        [sg.Button("Guardar", key="-SAVE-", bind_return_key=True), sg.Button("Cancelar", key="-CANCEL-")],
    ]
    return sg.Window("Categorías · Finanzas personales", layout, modal=True, finalize=True,
                     alpha_channel=0 if hidden else 1)


def create_transaction_window(kind, categories, hidden=False, transaction=None):
    """Build a transaction form, prefilled when editing an existing record."""
    editing = transaction is not None
    category_name = next((c.nombre for c in categories if editing and c.id == transaction.categoria_id), "")
    layout = [
        [sg.Text("Editar movimiento" if editing else ("Registrar ingreso" if kind == "Ingreso" else "Registrar gasto"), font=("Segoe UI", 16, "bold"))],
        [sg.Text("Título", size=(12, 1)), sg.Input(transaction.titulo if editing else "", key="-TITLE-", size=(36, 1))],
        [sg.Text("Monto en colones", size=(15, 1)), sg.Input(str(transaction.monto) if editing else "", key="-AMOUNT-", size=(20, 1))],
        [sg.Text("Monto positivo; hasta dos decimales, sin separadores de miles.")],
        [sg.Text("Categoría", size=(12, 1)), sg.Combo([c.nombre for c in categories], readonly=True,
                                                             default_value=category_name, key="-CATEGORY-", size=(34, 1))],
        [sg.Text("Tipo", size=(12, 1), visible=editing), sg.Combo(["Ingreso", "Gasto"], default_value=kind,
                                                readonly=True, key="-KIND-", size=(15, 1), visible=editing)],
        [sg.Text("Fecha", size=(12, 1)), sg.Input((transaction.fecha if editing else date.today()).strftime("%d/%m/%Y"), key="-DATE-", size=(15, 1))],
        [sg.Text("Formato: dd/mm/aaaa. La fecha no puede ser futura.")],
        [sg.Button("Guardar", key="-SAVE-", bind_return_key=True), sg.Button("Cancelar", key="-CANCEL-")],
    ]
    return sg.Window(f"{'Editar movimiento' if editing else kind} · Finanzas personales", layout, modal=True, finalize=True,
                     alpha_channel=0 if hidden else 1)


class FinanceApplication:
    """Manage windows and delegate all data changes and balances to the controller."""

    def __init__(self, controller, hidden=False):
        """Create the main table, category controls, filters, and balance cards."""
        self.controller = controller
        configure_theme()
        layout = [
            [sg.Text("Gestor de Finanzas Personales", font=("Segoe UI", 23, "bold"))],
            [sg.Text("Tus ingresos y gastos, en un solo lugar.  ·  Moneda: colón costarricense")],
            [sg.Frame("Ingresos visibles", [[sg.Text("", key="-INCOME-", size=(25, 1), font=("Segoe UI", 16, "bold"), text_color=ACCENT)]]),
             sg.Frame("Gastos visibles", [[sg.Text("", key="-EXPENSES-", size=(25, 1), font=("Segoe UI", 16, "bold"), text_color="#A13030")]]),
             sg.Frame("Balance visible", [[sg.Text("", key="-BALANCE-", size=(25, 1), font=("Segoe UI", 16, "bold"))]])],
            [sg.Button("Nuevo ingreso", key="-ADD-INCOME-", button_color=("white", ACCENT)),
             sg.Button("Nuevo gasto", key="-ADD-EXPENSE-"), sg.Button("Nueva categoría", key="-ADD-CATEGORY-")],
            [sg.Text("Editar categoría:"), sg.Combo([], key="-EDIT-SELECTION-", readonly=True, size=(28, 1)),
             sg.Button("Editar nombre / color", key="-EDIT-CATEGORY-")],
            [sg.HorizontalSeparator()],
            [sg.Text("Desde"), sg.Input(key="-START-", size=(13, 1)),
             sg.Text("Hasta"), sg.Input(key="-END-", size=(13, 1)),
             sg.Button("Filtrar", key="-FILTER-"), sg.Button("Quitar filtro", key="-CLEAR-FILTER-"),
             sg.Text("Fechas: dd/mm/aaaa")],
            [sg.Text("", key="-CONTEXT-", expand_x=True)],
            [sg.Table(values=[], headings=["Fecha", "Título", "Monto", "Categoría", "Tipo"],
                      key="-TABLE-", auto_size_columns=False, col_widths=[12, 34, 23, 24, 10],
                      justification="left", num_rows=14, row_height=29, expand_x=True, expand_y=True,
                      header_background_color=PRIMARY, header_text_color="#FFFFFF",
                      selected_row_colors=("#FFFFFF", ACCENT), select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
            [sg.Text("Seleccione un movimiento:"), sg.Button("Editar", key="-EDIT-TRANSACTION-"),
             sg.Button("Eliminar", key="-DELETE-TRANSACTION-")],
            [sg.Button("Exportar todo a CSV", key="-EXPORT-"), sg.Push(), sg.Button("Salir", key="-EXIT-")],
            [sg.Text("Guardado automático después de cada cambio. El CSV incluye todos los movimientos.", key="-STATUS-", expand_x=True)],
        ]
        self.window = sg.Window("Gestor de Finanzas Personales", layout, finalize=True, resizable=True,
                                margins=(18, 14), alpha_channel=0 if hidden else 1)
        self.refresh()

    def refresh(self, message=None):
        """Refresh rows, persistent category colors, and precomputed visible totals."""
        view = self.controller.get_view()
        self._transaction_ids = view.transaction_ids
        self.window["-TABLE-"].update(values=view.filas, row_colors=view.colores, select_rows=[])
        for key, value in (("-INCOME-", view.ingresos), ("-EXPENSES-", view.gastos),
                           ("-BALANCE-", view.balance), ("-CONTEXT-", view.resumen)):
            self.window[key].update(value)
        self.window["-EDIT-SELECTION-"].update(values=[c.nombre for c in self.controller.categories], value="")
        if message:
            self.window["-STATUS-"].update(message)
        self.window.refresh()

    def open_category_dialog(self, category=None):
        """Keep invalid category forms open so users can correct their input."""
        dialog = create_category_window(category)
        try:
            while True:
                event, values = dialog.read()
                if event in (sg.WIN_CLOSED, "-CANCEL-"):
                    return
                if event == "-SAVE-":
                    try:
                        self.controller.save_category(values["-NAME-"], values["-COLOR-"],
                                                          category.id if category else None)
                    except FinanceError as error:
                        show_error(error)
                    else:
                        self.refresh("Categoría guardada correctamente.")
                        return
        finally:
            dialog.close()

    def open_transaction_dialog(self, kind, transaction=None):
        """Reject missing categories before opening an income or expense form."""
        categories = self.controller.categories
        if not categories:
            show_error("Primero debe crear una categoría antes de registrar movimientos.")
            return
        dialog = (create_transaction_window(kind, categories, transaction=transaction)
                  if transaction is not None else create_transaction_window(kind, categories))
        ids = {c.nombre: c.id for c in categories}
        try:
            while True:
                event, values = dialog.read()
                if event in (sg.WIN_CLOSED, "-CANCEL-"):
                    return
                if event == "-SAVE-":
                    try:
                        self.controller.save_transaction(
                            values, values["-KIND-"] if transaction else kind, ids.get(values["-CATEGORY-"]),
                            transaction.id if transaction else None,
                        )
                    except FinanceError as error:
                        show_error(error)
                    else:
                        self.refresh("Movimiento actualizado correctamente." if transaction else f"{kind} guardado correctamente.")
                        return
        finally:
            dialog.close()

    def get_selected_transaction(self, values):
        """Resolve the selected row using the identities of the displayed snapshot."""
        selection = values.get("-TABLE-", [])
        if (len(selection) != 1 or type(selection[0]) is not int
                or not 0 <= selection[0] < len(self._transaction_ids)):
            raise ValidationError("Seleccione el movimiento que desea editar o eliminar.")
        return self.controller.get_transaction(self._transaction_ids[selection[0]])

    def handle_event(self, event, values):
        """Route main-window events; retain the previous view on validation errors."""
        try:
            if event == "-ADD-CATEGORY-":
                self.open_category_dialog()
            elif event == "-EDIT-CATEGORY-":
                category = next((c for c in self.controller.categories if c.nombre == values["-EDIT-SELECTION-"]), None)
                if category is None:
                    show_error("Seleccione la categoría que desea editar.")
                else:
                    self.open_category_dialog(category)
            elif event in ("-ADD-INCOME-", "-ADD-EXPENSE-"):
                self.open_transaction_dialog("Ingreso" if event == "-ADD-INCOME-" else "Gasto")
            elif event == "-EDIT-TRANSACTION-":
                movement = self.get_selected_transaction(values)
                self.open_transaction_dialog(movement.tipo, movement)
            elif event == "-DELETE-TRANSACTION-":
                movement = self.get_selected_transaction(values)
                answer = sg.popup(
                    f'¿Desea eliminar el movimiento "{movement.titulo}"?\n'
                    f"Fecha: {movement.fecha:%d/%m/%Y} · Tipo: {movement.tipo} · Monto: ₡ {movement.monto:.2f}\n"
                    "Esta acción no se puede deshacer.",
                    title="Confirmar eliminación", custom_text=("Confirmar", "Cancelar"), keep_on_top=True,
                )
                if answer == "Confirmar":
                    self.controller.delete_transaction(movement.id)
                    self.refresh("Movimiento eliminado correctamente.")
            elif event == "-FILTER-":
                self.controller.filter_by_date(values["-START-"], values["-END-"])
                self.refresh("Filtro aplicado. Los totales corresponden al intervalo visible.")
            elif event == "-CLEAR-FILTER-":
                self.controller.clear_filter()
                self.window["-START-"].update("")
                self.window["-END-"].update("")
                self.refresh("Se muestran todos los movimientos.")
            elif event == "-EXPORT-":
                path = sg.popup_get_file("Guardar todos los movimientos como CSV", title="Exportar CSV",
                                         save_as=True, default_extension=".csv", default_path="finanzas.csv",
                                         file_types=(("Archivo CSV", "*.csv"),), no_window=True)
                if path:
                    destination = self.controller.export(path)
                    self.refresh(f"CSV exportado correctamente: {destination}")
        except FinanceError as error:
            show_error(error)

    def run(self):
        """Run the event loop and always release the desktop window."""
        try:
            while True:
                event, values = self.window.read()
                if event in (sg.WIN_CLOSED, "-EXIT-"):
                    return
                self.handle_event(event, values)
        finally:
            self.window.close()
