"""
Student: Cesar Lanuza Urbina
Program: Verify filtered totals, persistent row colors, and view state without importing the GUI.
"""

import pytest

from finance_manager.controller import FinanceController
from finance_manager.errors import ValidationError


def test_get_view_category_color_tc027(manager, category):
    """Refresh all rows when their shared category color changes."""
    # Arrange
    manager.record_transaction("Compra", "1", category.id, "Gasto", "22/10/2026")
    controller = FinanceController(manager)
    # Act
    controller.save_category("Actualizada", "#000000", category.id)
    view = controller.get_view()
    # Assert
    assert view.colores == [(0, "#FFFFFF", "#000000")]
    assert view.filas[0][3] == "Actualizada"
    assert "-1,00" in view.filas[0][2]


def test_filter_by_date_invalid_preserves_view_tc028(manager, category):
    """Leave a valid active filter unchanged if another filter is invalid."""
    # Arrange
    manager.record_transaction("Compra", "1", category.id, "Gasto", "22/10/2026")
    controller = FinanceController(manager)
    controller.filter_by_date("01/10/2026", "02/10/2026")
    before = controller.get_view()
    # Act
    with pytest.raises(ValidationError):
        controller.filter_by_date("22/10/2026", "01/10/2026")
    # Assert
    assert controller.get_view() == before


def test_clear_filter_restores_totals_tc029(manager, category):
    """Show zero filtered totals and restore complete totals on filter removal."""
    # Arrange
    manager.record_transaction("Salario", "25", category.id, "Ingreso", "22/10/2026")
    controller = FinanceController(manager)
    controller.filter_by_date("01/10/2026", "02/10/2026")
    empty = controller.get_view()
    # Act
    controller.clear_filter()
    restored = controller.get_view()
    # Assert
    assert empty.filas == []
    assert empty.balance == "₡ 0,00"
    assert restored.balance == "₡ 25,00"