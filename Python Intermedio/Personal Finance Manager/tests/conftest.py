"""
Student: Cesar Lanuza Urbina
Program: Provide isolated finance services and deterministic test dates for pytest.
"""

from datetime import date

import pytest

from finance_manager.logic import FinanceManager
from finance_manager.persistence import FinanceRepository

TODAY = date(2026, 10, 22)


@pytest.fixture
def repository(tmp_path):
    """Keep every test's JSON file in its own temporary directory."""
    return FinanceRepository(tmp_path / "finanzas.json", today=lambda: TODAY)


@pytest.fixture
def manager(repository):
    """Provide an empty service with a stable clock."""
    return FinanceManager(repository, today=lambda: TODAY)


@pytest.fixture
def category(manager):
    """Create one valid category for transaction tests."""
    return manager.create_category("General", "#DCEEF8")