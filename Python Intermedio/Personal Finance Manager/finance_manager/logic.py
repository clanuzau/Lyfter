"""
Student: Cesar Lanuza Urbina
Program: Manage categories, transactions, date filtering, and exact financial totals.
"""

from datetime import date
from decimal import Decimal
from uuid import uuid4

from .errors import ValidationError
from .models import Category, FinanceState, Transaction, Totals
from .validation import validate_color, validate_date, validate_amount, validate_date_range, validate_text


class FinanceManager:
    """Apply business rules and commit state only after persistence succeeds."""

    def __init__(self, repository, today=None):
        """Restore the last saved state before accepting any changes."""
        self.repository = repository
        self.today = today or date.today
        self._state = repository.load()

    @property
    def categories(self):
        """Expose immutable category records."""
        return self._state.categories

    @property
    def transactions(self):
        """Expose immutable transaction records."""
        return self._state.transactions

    def _commit(self, state):
        """Save first so a failed disk operation cannot change in-memory state."""
        self.repository.save(state)
        self._state = state

    def _category_values(self, name, color, excluding=None):
        """Validate category fields and case-insensitive name uniqueness."""
        name = validate_text(name, "nombre de categoría", 60)
        color = validate_color(color)
        if any(c.nombre.casefold() == name.casefold() and c.id != excluding for c in self.categories):
            raise ValidationError("Ya existe una categoría con ese nombre.")
        return name, color

    def create_category(self, name, color):
        """Create and immediately persist a category shared by both transaction types."""
        name, color = self._category_values(name, color)
        category = Category(str(uuid4()), name, color)
        self._commit(FinanceState(self.categories + (category,), self.transactions))
        return category

    def edit_category(self, category_id, name, color):
        """Update category appearance while preserving all transaction references."""
        if not any(c.id == category_id for c in self.categories):
            raise ValidationError("Seleccione una categoría existente.")
        name, color = self._category_values(name, color, category_id)
        updated = Category(category_id, name, color)
        categories = tuple(updated if c.id == category_id else c for c in self.categories)
        self._commit(FinanceState(categories, self.transactions))
        return updated

    def _build_transaction(self, transaction_id, title, amount, category_id, kind, date_text):
        """Apply the same field validation to new and edited transactions."""
        if not self.categories:
            raise ValidationError("Primero debe crear una categoría antes de registrar movimientos.")
        if not any(c.id == category_id for c in self.categories):
            raise ValidationError("Seleccione una categoría existente.")
        if kind not in ("Ingreso", "Gasto"):
            raise ValidationError("El tipo debe ser Ingreso o Gasto.")
        return Transaction(
            transaction_id, validate_date(date_text, self.today()),
            validate_text(title, "título"), validate_amount(amount), category_id, kind,
        )

    def record_transaction(self, title, amount, category_id, kind, date_text):
        """Validate and save a positive income or expense with a nonfuture date."""
        movement = self._build_transaction(str(uuid4()), title, amount, category_id, kind, date_text)
        self._commit(FinanceState(self.categories, self.transactions + (movement,)))
        return movement

    def get_transaction(self, transaction_id):
        """Resolve a stable identity or reject a missing transaction."""
        movement = next((m for m in self.transactions if m.id == transaction_id), None)
        if movement is None:
            raise ValidationError("Seleccione un movimiento existente.")
        return movement

    def edit_transaction(self, transaction_id, title, amount, category_id, kind, date_text):
        """Persist replacement fields while preserving identity and collection order."""
        self.get_transaction(transaction_id)
        updated = self._build_transaction(transaction_id, title, amount, category_id, kind, date_text)
        movements = tuple(updated if m.id == transaction_id else m for m in self.transactions)
        self._commit(FinanceState(self.categories, movements))
        return updated

    def delete_transaction(self, transaction_id):
        """Persist removal of an existing transaction before updating memory."""
        self.get_transaction(transaction_id)
        movements = tuple(m for m in self.transactions if m.id != transaction_id)
        self._commit(FinanceState(self.categories, movements))

    def query_transactions(self, start=None, end=None):
        """Return transactions ordered by date, including both filter boundaries."""
        movements = self.transactions
        if start is not None or end is not None:
            if not start or not end:
                raise ValidationError("Complete ambas fechas para filtrar.")
            first, last = validate_date_range(start, end)
            movements = tuple(m for m in movements if first <= m.fecha <= last)
        return tuple(sorted(movements, key=lambda m: m.fecha, reverse=True))

    def calculate_totals(self, movements=None):
        """Calculate totals for all records or a supplied filtered collection."""
        items = self.transactions if movements is None else tuple(movements)
        income = sum((m.monto for m in items if m.tipo == "Ingreso"), Decimal("0.00"))
        expenses = sum((m.monto for m in items if m.tipo == "Gasto"), Decimal("0.00"))
        return Totals(income, expenses)
