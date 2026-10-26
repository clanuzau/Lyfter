"""
Student: Cesar Lanuza Urbina
Program: Verify categories, monetary rules, transaction dates, filtering, and exact balances without a GUI.
"""

from datetime import date
from decimal import Decimal
from unittest.mock import patch

import pytest

from finance_manager.errors import PersistenceError, ValidationError
from finance_manager.logic import FinanceManager


def test_create_category_valid_values_tc001(manager):
    """Store a trimmed name and normalized hexadecimal color."""
    # Arrange
    name, color = "  Alimentación  ", "#aabbcc"
    # Act
    category = manager.create_category(name, color)
    # Assert
    assert (category.nombre, category.color) == ("Alimentación", "#AABBCC")
    assert manager.categories == (category,)


@pytest.mark.parametrize("name", ["", "   ", "General", "GENERAL", "general"])
def test_create_category_invalid_name_tc002(manager, category, name):
    """Reject empty or duplicate names without changing state."""
    # Arrange
    before = manager.categories
    # Act
    with pytest.raises(ValidationError):
        manager.create_category(name, "#FFFFFF")
    # Assert
    assert manager.categories == before


@pytest.mark.parametrize("color", ["red", "#FFF", "#GGGGGG", "", None])
def test_create_category_invalid_color_tc003(manager, color):
    """Reject unsupported color names and malformed hexadecimal values."""
    # Arrange
    before = manager.categories
    # Act
    with pytest.raises(ValidationError):
        manager.create_category("Prueba", color)
    # Assert
    assert manager.categories == before


def test_record_transaction_income_tc004(manager, category):
    """Record income and update the balance with an exact positive amount."""
    # Arrange
    expected = Decimal("1000.25")
    # Act
    movement = manager.record_transaction("Salario", "1000,25", category.id, "Ingreso", "22/10/2026")
    totals = manager.calculate_totals()
    # Assert
    assert movement.monto == expected
    assert totals.ingresos == totals.balance == expected
    assert totals.gastos == Decimal("0.00")


def test_record_transaction_expense_tc005(manager, category):
    """Keep stored expenses positive and show a negative signed amount."""
    # Arrange
    expected = Decimal("25.10")
    # Act
    movement = manager.record_transaction("Comida", "25.10", category.id, "Gasto", "21/10/2026")
    totals = manager.calculate_totals()
    # Assert
    assert movement.monto == totals.gastos == expected
    assert movement.signed_amount == totals.balance == -expected


def test_record_transaction_no_category_tc006(manager):
    """Reject movements when no category exists."""
    # Arrange
    before = manager.transactions
    # Act
    with pytest.raises(ValidationError, match="crear una categoría"):
        manager.record_transaction("Compra", "10", "missing", "Gasto", "22/10/2026")
    # Assert
    assert manager.transactions == before


@pytest.mark.parametrize("amount", ["0", "-1", "texto", "NaN", "Infinity", "1.001", "1,000.50", True, "1000000000000"])
def test_record_transaction_invalid_amount_tc007(manager, category, amount):
    """Reject nonpositive, nonfinite, malformed, or excessive amounts."""
    # Arrange
    before = manager.transactions
    # Act
    with pytest.raises(ValidationError):
        manager.record_transaction("Compra", amount, category.id, "Gasto", "22/10/2026")
    # Assert
    assert manager.transactions == before


@pytest.mark.parametrize("date_text", ["31/02/2026", "23/10/2026", "2026-10-22", "1/10/2026", ""])
def test_record_transaction_invalid_date_tc008(manager, category, date_text):
    """Reject invalid dates, future dates, and noncanonical display formats."""
    # Arrange
    before = manager.transactions
    # Act
    with pytest.raises(ValidationError):
        manager.record_transaction("Compra", "10", category.id, "Gasto", date_text)
    # Assert
    assert manager.transactions == before


def test_query_transactions_inclusive_bounds_tc009(manager, category):
    """Include both interval boundaries and exclude records outside them."""
    # Arrange
    for day in (1, 10, 15, 20):
        manager.record_transaction(str(day), "1", category.id, "Ingreso", f"{day:02d}/10/2026")
    # Act
    result = manager.query_transactions("10/10/2026", "15/10/2026")
    # Assert
    assert [m.fecha for m in result] == [date(2026, 10, 15), date(2026, 10, 10)]
    assert len(manager.transactions) == 4


@pytest.mark.parametrize("start,end", [("20/10/2026", "10/10/2026"), ("incorrecta", "22/10/2026"), ("", "22/10/2026")])
def test_query_transactions_invalid_range_tc010(manager, category, start, end):
    """Reject invalid filters without modifying stored transactions."""
    # Arrange
    manager.record_transaction("Compra", "1", category.id, "Gasto", "22/10/2026")
    before = manager.transactions
    # Act
    with pytest.raises(ValidationError):
        manager.query_transactions(start, end)
    # Assert
    assert manager.transactions == before


def test_edit_category_preserves_reference_tc011(manager, category):
    """Persist edited names and colors while retaining transaction links."""
    # Arrange
    movement = manager.record_transaction("Compra", "1", category.id, "Gasto", "22/10/2026")
    # Act
    updated = manager.edit_category(category.id, "Comida", "#AABBCC")
    restored = FinanceManager(manager.repository)
    # Assert
    assert updated.id == movement.categoria_id
    assert restored.categories[0] == updated
    assert restored.transactions == (movement,)


def test_calculate_totals_decimal_precision_tc012(manager, category):
    """Avoid binary floating-point errors when combining decimal amounts."""
    # Arrange
    for amount in ("0.10", "0.20"):
        manager.record_transaction("Abono", amount, category.id, "Ingreso", "22/10/2026")
    manager.record_transaction("Gasto", "0.05", category.id, "Gasto", "22/10/2026")
    # Act
    totals = manager.calculate_totals()
    # Assert
    assert totals.ingresos == Decimal("0.30")
    assert totals.gastos == Decimal("0.05")
    assert totals.balance == Decimal("0.25")


def test_commit_failed_save_keeps_state_tc013(manager, category):
    """Keep both disk and memory unchanged when a save fails."""
    # Arrange
    before = manager.repository.path.read_bytes()
    with patch.object(manager.repository, 'save', side_effect=PersistenceError("Error de prueba")):
        # Act
        with pytest.raises(PersistenceError):
            manager.record_transaction("Compra", "1", category.id, "Gasto", "22/10/2026")
    # Assert
    assert manager.transactions == ()
    assert manager.repository.path.read_bytes() == before


@pytest.mark.parametrize("field,value", [("title", ""), ("kind", "Otro"), ("category", "missing")])
def test_record_transaction_invalid_fields_tc014(manager, category, field, value):
    """Reject missing titles, unknown types, and nonexistent category references."""
    # Arrange
    values = {"title": "Compra", "kind": "Gasto", "category": category.id}
    values[field] = value
    # Act
    with pytest.raises(ValidationError):
        manager.record_transaction(values["title"], "1", values["category"], values["kind"], "22/10/2026")
    # Assert
    assert manager.transactions == ()


def test_record_transaction_repeated_titles_tc015(manager, category):
    """Allow repeated transaction titles with distinct identities."""
    # Arrange
    title = "Compra"
    # Act
    first = manager.record_transaction(title, "1", category.id, "Gasto", "22/10/2026")
    second = manager.record_transaction(title, "2", category.id, "Gasto", "22/10/2026")
    # Assert
    assert first.id != second.id
    assert len(manager.transactions) == 2