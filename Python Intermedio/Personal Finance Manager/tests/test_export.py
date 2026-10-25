"""
Student: Cesar Lanuza Urbina
Program: Verify CSV columns, signed amounts, full exports, totals, and write protection.
"""

import csv
from unittest.mock import patch

import pytest

from finance_manager.controller import FinanceController
from finance_manager.errors import ExportError, ValidationError


def test_export_complete_csv_tc022(manager, category, tmp_path):
    """Export all records and exact totals even while a date filter is active."""
    # Arrange
    manager.record_transaction("Salario", "100.30", category.id, "Ingreso", "01/10/2026")
    manager.record_transaction("Café", "20.10", category.id, "Gasto", "22/10/2026")
    controller = FinanceController(manager)
    controller.filter_by_date("22/10/2026", "22/10/2026")
    path = tmp_path / "resumen.csv"
    # Act
    controller.export(path)
    with path.open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.reader(file))
    # Assert
    assert rows[0] == ["Fecha", "Título", "Monto", "Categoría", "Tipo"]
    assert rows[1][1:3] == ["Café", "-20.10"]
    assert rows[2][1:3] == ["Salario", "100.30"]
    assert [r[2] for r in rows[-3:]] == ["100.30", "20.10", "80.20"]
    assert path.read_bytes().startswith(b"\xef\xbb\xbf")
    assert len(controller.get_view().filas) == 1


def test_export_empty_state_tc023(manager, tmp_path):
    """Export an empty table with zero totals."""
    # Arrange
    controller = FinanceController(manager)
    path = tmp_path / "vacio.csv"
    # Act
    controller.export(path)
    with path.open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.reader(file))
    # Assert
    assert [r[2] for r in rows[-3:]] == ["0.00", "0.00", "0.00"]


def test_export_formula_text_tc024(manager, tmp_path):
    """Prevent user-provided text from becoming a spreadsheet formula."""
    # Arrange
    category = manager.create_category("=1+1", "#FFFFFF")
    manager.record_transaction("@SUM(A1)", "1", category.id, "Ingreso", "22/10/2026")
    path = tmp_path / "formulas.csv"
    # Act
    FinanceController(manager).export(path)
    with path.open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.reader(file))
    # Assert
    assert rows[1][1] == "'@SUM(A1)"
    assert rows[1][3] == "'=1+1"


def test_export_reject_data_destination_tc025(manager, category):
    """Do not allow a CSV export to overwrite the JSON state."""
    # Arrange
    before = manager.repository.path.read_bytes()
    # Act
    with pytest.raises(ValidationError):
        FinanceController(manager).export(manager.repository.path)
    # Assert
    assert manager.repository.path.read_bytes() == before


def test_export_failed_replace_tc026(manager, category, tmp_path):
    """Keep an existing CSV intact if the replacement fails."""
    # Arrange
    path = tmp_path / "existente.csv"
    path.write_text("contenido anterior", encoding="utf-8")
    with patch("finance_manager.export.os.replace", side_effect=PermissionError):
        # Act
        with pytest.raises(ExportError):
            FinanceController(manager).export(path)
    # Assert
    assert path.read_text(encoding="utf-8") == "contenido anterior"
    assert not list(tmp_path.glob(".export-*.tmp"))