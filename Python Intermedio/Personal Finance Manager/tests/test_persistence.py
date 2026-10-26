"""
Student: Cesar Lanuza Urbina
Program: Verify restoration, corrupt data protection, schema validation, and atomic write failures.
"""

import json
from unittest.mock import patch

import pytest

from finance_manager.errors import PersistenceError
from finance_manager.logic import FinanceManager
from finance_manager.models import FinanceState


def test_load_missing_file_tc016(repository):
    """Start empty without creating a data file during loading."""
    # Arrange
    path = repository.path
    # Act
    state = repository.load()
    # Assert
    assert state == FinanceState()
    assert not path.exists()


def test_load_saved_state_tc017(manager, category):
    """Restore all categories, colors, dates, and exact amounts after restart."""
    # Arrange
    movement = manager.record_transaction("Salario", "123.45", category.id, "Ingreso", "22/10/2026")
    # Act
    restored = FinanceManager(manager.repository)
    # Assert
    assert restored.categories == (category,)
    assert restored.transactions == (movement,)


@pytest.mark.parametrize("content", ["{corrupto", "[]", '{"version": 9}', '{"version": true}', '{"version":1,"categorias":null,"movimientos":[]}'])
def test_load_corrupt_file_never_overwritten_tc018(repository, content):
    """Block subsequent saving after an unreadable or invalid state file."""
    # Arrange
    repository.path.write_text(content, encoding="utf-8")
    # Act
    with pytest.raises(PersistenceError):
        repository.load()
    with pytest.raises(PersistenceError):
        repository.save(FinanceState())
    # Assert
    assert repository.path.read_text(encoding="utf-8") == content


@pytest.mark.parametrize("change", ["duplicate", "reference", "amount", "future", "type"])
def test_load_invalid_record_tc019(manager, category, change):
    """Validate duplicate categories and invalid persisted transaction fields."""
    # Arrange
    manager.record_transaction("Compra", "1", category.id, "Gasto", "22/10/2026")
    path = manager.repository.path
    raw = json.loads(path.read_text(encoding="utf-8"))
    if change == "duplicate":
        raw["categorias"].append(raw["categorias"][0])
    else:
        field, value = {"reference": ("categoria_id", "missing"), "amount": ("monto", "-2"),
                        "future": ("fecha", "2026-10-23"), "type": ("tipo", "Otro")}[change]
        raw["movimientos"][0][field] = value
    original = json.dumps(raw)
    path.write_text(original, encoding="utf-8")
    # Act
    with pytest.raises(PersistenceError):
        manager.repository.load()
    # Assert
    assert path.read_text(encoding="utf-8") == original


def test_save_replace_failure_tc020(manager, category):
    """Preserve the previous state and clean temporary files on replace failure."""
    # Arrange
    before = manager.repository.path.read_bytes()
    with patch("finance_manager.persistence.os.replace", side_effect=PermissionError):
        # Act
        with pytest.raises(PersistenceError):
            manager.create_category("Otra", "#FFFFFF")
    # Assert
    assert manager.repository.path.read_bytes() == before
    assert manager.categories == (category,)
    assert not list(manager.repository.path.parent.glob(".finanzas-*.tmp"))


def test_load_permission_failure_tc021(repository):
    """Report inaccessible files rather than silently initializing empty state."""
    # Arrange
    with patch("pathlib.Path.open", side_effect=PermissionError):
        # Act
        with pytest.raises(PersistenceError):
            repository.load()
    # Assert
    with pytest.raises(PersistenceError):
        repository.save(FinanceState())

def test_load_legacy_json_after_method_rename_tc032(repository):
    """Keep the existing JSON schema readable and writable through the English API."""
    # Arrange
    original = {
        "version": 1,
        "categorias": [{"id": "category-1", "nombre": "General", "color": "#DCEEF8"}],
        "movimientos": [{
            "id": "transaction-1", "fecha": "2026-10-22", "titulo": "Salario",
            "monto": "10.25", "categoria_id": "category-1", "tipo": "Ingreso",
        }],
    }
    repository.path.write_text(json.dumps(original, ensure_ascii=False), encoding="utf-8")
    expected = json.loads(json.dumps(original))
    expected["categorias"][0].update(nombre="Trabajo", color="#112233")

    # Act
    restored = FinanceManager(repository)
    restored.edit_category("category-1", "Trabajo", "#112233")
    saved = json.loads(repository.path.read_text(encoding="utf-8"))
    reloaded = FinanceManager(repository)

    # Assert
    assert saved == expected
    assert reloaded.categories == restored.categories
    assert reloaded.transactions == restored.transactions
    assert reloaded.transactions[0].signed_amount == restored.calculate_totals().balance