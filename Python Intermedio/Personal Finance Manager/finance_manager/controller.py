"""
Student: Cesar Lanuza Urbina
Program: Coordinate user actions and prepare finance data for the desktop interface.
"""

from dataclasses import dataclass
from pathlib import Path

from .errors import ValidationError
from .export import CSVExporter


def format_currency(value):
    """Format CRC amounts with Spanish separators and two decimal places."""
    return "₡ " + f"{value:,.2f}".translate(str.maketrans({",": ".", ".": ","}))


def text_color(background):
    """Choose a readable foreground for each category background."""
    red, green, blue = (int(background[i:i + 2], 16) for i in (1, 3, 5))
    return "#142230" if red * 299 + green * 587 + blue * 114 > 150000 else "#FFFFFF"


@dataclass(frozen=True)
class FinanceView:
    """Carry ready-to-display rows, styles, totals, and filter context."""
    filas: list
    colores: list
    ingresos: str
    gastos: str
    balance: str
    resumen: str
    transaction_ids: tuple[str, ...]


class FinanceController:
    """Separate event handling and presentation data from business calculations."""

    def __init__(self, manager, exporter=None):
        """Keep service dependencies and the active date filter."""
        self.manager = manager
        self.exporter = exporter or CSVExporter()
        self._filter = (None, None)

    @property
    def categories(self):
        """Return categories in a stable alphabetical display order."""
        return tuple(sorted(self.manager.categories, key=lambda c: c.nombre.casefold()))

    def save_category(self, name, color, category_id=None):
        """Route category creation or editing to the finance service."""
        if category_id is None:
            return self.manager.create_category(name, color)
        return self.manager.edit_category(category_id, name, color)

    def save_transaction(self, values, kind, category_id, transaction_id=None):
        """Translate modal form values into a validated service operation."""
        if transaction_id is not None:
            return self.manager.edit_transaction(
                transaction_id, values["-TITLE-"], values["-AMOUNT-"], category_id, kind, values["-DATE-"],
            )
        return self.manager.record_transaction(
            values["-TITLE-"], values["-AMOUNT-"], category_id, kind, values["-DATE-"],
        )

    def get_transaction(self, transaction_id):
        """Retrieve the transaction selected by its stable identity."""
        return self.manager.get_transaction(transaction_id)

    def delete_transaction(self, transaction_id):
        """Delete a transaction after the interface confirms the action."""
        self.manager.delete_transaction(transaction_id)

    def filter_by_date(self, start, end):
        """Change the active filter only if both bounds are valid."""
        if not start and not end:
            raise ValidationError("Complete ambas fechas o use Quitar filtro.")
        self.manager.query_transactions(start, end)
        self._filter = (start, end)

    def clear_filter(self):
        """Restore the complete transaction view."""
        self._filter = (None, None)

    def get_view(self):
        """Prepare signed table rows and totals for the visible interval."""
        movements = self.manager.query_transactions(*self._filter)
        categories = {c.id: c for c in self.manager.categories}
        rows, colors = [], []
        for index, movement in enumerate(movements):
            category = categories[movement.categoria_id]
            rows.append([
                movement.fecha.strftime("%d/%m/%Y"), movement.titulo,
                format_currency(movement.signed_amount), category.nombre, movement.tipo,
            ])
            colors.append((index, text_color(category.color), category.color))
        totals = self.manager.calculate_totals(movements)
        context = "Todos los movimientos" if self._filter[0] is None else f"Del {self._filter[0]} al {self._filter[1]}"
        return FinanceView(rows, colors, format_currency(totals.ingresos),
                            format_currency(totals.gastos), format_currency(totals.balance),
                            f"{context} · {len(rows)} movimiento(s)",
                            tuple(m.id for m in movements))

    def export(self, path):
        """Always export all transactions, regardless of the active date filter."""
        destination = Path(path).resolve()
        if destination == self.manager.repository.path:
            raise ValidationError("El CSV no puede reemplazar el archivo de datos del programa.")
        if destination.suffix.lower() != ".csv":
            raise ValidationError("Seleccione un archivo con extensión .csv.")
        return self.exporter.export(destination, self.manager.query_transactions(),
                                     self.manager.categories, self.manager.calculate_totals())
