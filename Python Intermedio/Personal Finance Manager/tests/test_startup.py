"""
Student: Cesar Lanuza Urbina
Program: Verify that the application prevents concurrent writes and releases its instance lock.
"""

import pytest

from main import SingleInstanceLock
from finance_manager.errors import FinanceError


def test_single_instance_lock_second_instance_tc030(tmp_path):
    """Reject a second active writer for the same data path."""
    # Arrange
    path = tmp_path / "finanzas.lock"
    # Act
    with SingleInstanceLock(path):
        with pytest.raises(FinanceError, match="ya está abierto"):
            with SingleInstanceLock(path):
                pytest.fail("Se permitió una segunda instancia.")
    # Assert
    assert path.exists()


def test_single_instance_lock_released_after_error_tc031(tmp_path):
    """Release the OS lock after an exception so a later launch succeeds."""
    # Arrange
    path = tmp_path / "finanzas.lock"
    # Act
    with pytest.raises(ValueError):
        with SingleInstanceLock(path):
            raise ValueError("Error de prueba")
    with SingleInstanceLock(path) as acquired:
        reopened = acquired.file is not None
    # Assert
    assert reopened