"""
Student: Cesar Lanuza Urbina
Program: Verify transaction updates, deletion, persistence, selection, and confirmation flows.
"""

import csv
from datetime import date
from decimal import Decimal
from unittest.mock import MagicMock, patch

import pytest

from finance_manager.controller import FinanceController
from finance_manager.errors import PersistenceError, ValidationError
from finance_manager.interface import FinanceApplication
from finance_manager.logic import FinanceManager


@pytest.fixture
def movement(manager, category):
    """Create a record whose fields can be edited or removed."""
    return manager.record_transaction("Compra", "10", category.id, "Gasto", "22/10/2026")


def test_edit_transaction_persists_all_fields(manager, category, movement):
    """Keep identity and other records while updating every editable field."""
    other = manager.record_transaction("Compra", "5", category.id, "Gasto", "22/10/2026")
    new_category = manager.create_category("Salario", "#FFFFFF")

    updated = manager.edit_transaction(movement.id, " Abono ", "25,50", new_category.id,
                                       "Ingreso", "20/10/2026")
    restored = FinanceManager(manager.repository)

    assert updated.id == movement.id
    assert (updated.titulo, updated.monto, updated.categoria_id, updated.tipo, updated.fecha) == (
        "Abono", Decimal("25.50"), new_category.id, "Ingreso", date(2026, 10, 20),
    )
    assert restored.transactions == manager.transactions == (updated, other)
    assert manager.calculate_totals().balance == Decimal("20.50")


@pytest.mark.parametrize("field,value", [
    ("title", ""), ("amount", "0"), ("amount", "1.001"), ("category_id", "missing"),
    ("kind", "Otro"), ("date_text", "23/10/2026"), ("date_text", "31/02/2026"),
])
def test_edit_transaction_invalid_fields_preserve_state(manager, category, movement, field, value):
    """Reuse creation rules and leave disk and memory intact on invalid edits."""
    before = manager.repository.path.read_bytes()
    fields = dict(title="Actualizado", amount="20", category_id=category.id,
                  kind="Ingreso", date_text="22/10/2026")
    fields[field] = value

    with pytest.raises(ValidationError):
        manager.edit_transaction(movement.id, **fields)

    assert manager.transactions == (movement,)
    assert manager.repository.path.read_bytes() == before


def test_delete_transaction_persists_and_updates_export(manager, category, movement, tmp_path):
    """Delete only the selected identity even when titles repeat, including after reload."""
    other = manager.record_transaction("Compra", "5", category.id, "Ingreso", "22/10/2026")

    manager.delete_transaction(movement.id)
    restored = FinanceManager(manager.repository)
    path = FinanceController(restored).export(tmp_path / "updated.csv")

    assert restored.transactions == manager.transactions == (other,)
    assert restored.calculate_totals().balance == Decimal("5.00")
    with path.open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.reader(file))
    assert rows[1][1:3] == ["Compra", "5.00"]
    assert len(rows) == 6
    manager.delete_transaction(other.id)
    assert FinanceManager(manager.repository).transactions == ()
    assert manager.calculate_totals().balance == 0


@pytest.mark.parametrize("operation", ["edit", "delete"])
def test_transaction_change_missing_identity(manager, category, movement, operation):
    """Reject stale identities without writing or affecting existing records."""
    before = manager.repository.path.read_bytes()

    with patch.object(manager.repository, "save") as save:
        with pytest.raises(ValidationError, match="movimiento existente"):
            if operation == "edit":
                manager.edit_transaction("missing", "Otro", "1", category.id, "Ingreso", "22/10/2026")
            else:
                manager.delete_transaction("missing")

    save.assert_not_called()
    assert manager.transactions == (movement,)
    assert manager.repository.path.read_bytes() == before


@pytest.mark.parametrize("operation", ["edit", "delete"])
def test_transaction_change_failed_replace_preserves_state(manager, category, movement, operation):
    """An actual atomic replacement failure must retain the saved data and memory."""
    before = manager.repository.path.read_bytes()

    with patch("finance_manager.persistence.os.replace", side_effect=PermissionError):
        with pytest.raises(PersistenceError):
            if operation == "edit":
                manager.edit_transaction(movement.id, "Otro", "1", category.id, "Ingreso", "22/10/2026")
            else:
                manager.delete_transaction(movement.id)

    assert manager.transactions == (movement,)
    assert manager.repository.path.read_bytes() == before
    assert not list(manager.repository.path.parent.glob(".finanzas-*.tmp"))


@pytest.fixture
def application(manager):
    """Use real handlers and services with a mocked window to avoid opening a GUI."""
    app = FinanceApplication.__new__(FinanceApplication)
    app.controller = FinanceController(manager)
    app.window = MagicMock()
    app.refresh()
    return app


def test_edit_selected_filtered_transaction(application, manager, category, movement):
    """Resolve filtered row zero to its ID and refresh totals when its new date leaves the filter."""
    manager.record_transaction("Compra", "5", category.id, "Gasto", "20/10/2026")
    application.controller.filter_by_date("22/10/2026", "22/10/2026")
    application.refresh()
    dialog = MagicMock()
    dialog.read.return_value = ("-SAVE-", {
        "-TITLE-": "Editado", "-AMOUNT-": "30", "-CATEGORY-": category.nombre,
        "-KIND-": "Ingreso", "-DATE-": "21/10/2026",
    })

    with patch("finance_manager.interface.create_transaction_window", return_value=dialog) as factory:
        application.handle_event("-EDIT-TRANSACTION-", {"-TABLE-": [0]})

    factory.assert_called_once_with("Gasto", application.controller.categories, transaction=movement)
    dialog.close.assert_called_once()
    assert manager.get_transaction(movement.id).titulo == "Editado"
    assert application.controller.get_view().filas == []
    assert application.controller.get_view().balance == "₡ 0,00"
    assert application._transaction_ids == ()


@pytest.mark.parametrize("answer", ["Confirmar", "Cancelar", None])
def test_delete_requires_explicit_confirmation(application, manager, category, movement, answer):
    """Cancel or close the popup without writing; confirm removes only the visible record."""
    other = manager.record_transaction("Compra", "5", category.id, "Ingreso", "21/10/2026")
    application.controller.filter_by_date("22/10/2026", "22/10/2026")
    application.refresh()
    before = manager.repository.path.read_bytes()

    with patch("finance_manager.interface.sg.popup", autospec=True, return_value=answer) as popup:
        application.handle_event("-DELETE-TRANSACTION-", {"-TABLE-": [0]})

    assert popup.call_args.kwargs["custom_text"] == ("Confirmar", "Cancelar")
    assert movement.titulo in popup.call_args.args[0]
    if answer == "Confirmar":
        assert FinanceManager(manager.repository).transactions == (other,)
        assert application.controller.get_view().balance == "₡ 0,00"
    else:
        assert manager.transactions == (movement, other)
        assert manager.repository.path.read_bytes() == before


@pytest.mark.parametrize("event", ["-EDIT-TRANSACTION-", "-DELETE-TRANSACTION-"])
@pytest.mark.parametrize("selection", [[], [-1], [99]])
def test_transaction_action_requires_valid_selection(application, movement, event, selection):
    """Reject empty and stale row selections before opening any action dialog."""
    application.refresh()

    with patch("finance_manager.interface.show_error") as error, \
            patch("finance_manager.interface.sg.popup") as popup, \
            patch.object(application, "open_transaction_dialog") as edit:
        application.handle_event(event, {"-TABLE-": selection})

    error.assert_called_once()
    popup.assert_not_called()
    edit.assert_not_called()


@pytest.mark.parametrize("event", ["-CANCEL-", None])
def test_edit_cancel_preserves_record(application, manager, movement, event):
    """Cancel or close the editing form without saving changes."""
    application.refresh()
    before = manager.repository.path.read_bytes()
    dialog = MagicMock()
    dialog.read.return_value = (event, {})

    with patch("finance_manager.interface.create_transaction_window", return_value=dialog):
        application.handle_event("-EDIT-TRANSACTION-", {"-TABLE-": [0]})

    assert manager.transactions == (movement,)
    assert manager.repository.path.read_bytes() == before
    dialog.close.assert_called_once()


def test_edit_invalid_input_can_be_corrected(application, manager, category, movement):
    """Keep the modal open after validation fails and persist the corrected input."""
    application.refresh()
    values = {"-TITLE-": "Corregido", "-AMOUNT-": "20", "-CATEGORY-": category.nombre,
              "-KIND-": "Ingreso", "-DATE-": "22/10/2026"}
    dialog = MagicMock()
    dialog.read.side_effect = [("-SAVE-", dict(values, **{"-AMOUNT-": "0"})), ("-SAVE-", values)]

    with patch("finance_manager.interface.create_transaction_window", return_value=dialog), \
            patch("finance_manager.interface.show_error") as error:
        application.handle_event("-EDIT-TRANSACTION-", {"-TABLE-": [0]})

    error.assert_called_once()
    assert dialog.read.call_count == 2
    assert manager.get_transaction(movement.id).monto == Decimal("20.00")
    assert application.controller.get_view().balance == "₡ 20,00"
    dialog.close.assert_called_once()


def test_delete_failed_save_reports_error_without_refresh(application, manager, movement):
    """Keep the current table and record when confirmed deletion cannot be saved."""
    application.refresh()
    before = manager.repository.path.read_bytes()

    with patch("finance_manager.interface.sg.popup", return_value="Confirmar"), \
            patch("finance_manager.interface.show_error") as error, \
            patch.object(manager.repository, "save", side_effect=PersistenceError("No se pudo guardar.")), \
            patch.object(application, "refresh") as refresh:
        application.handle_event("-DELETE-TRANSACTION-", {"-TABLE-": [0]})

    error.assert_called_once()
    refresh.assert_not_called()
    assert manager.transactions == (movement,)
    assert manager.repository.path.read_bytes() == before
