"""
Student: Cesar Lanuza Urbina
Program: Define user-facing errors for finance validation and file operations.
"""

class FinanceError(Exception):
    """Represent a recoverable application error with a Spanish message."""


class ValidationError(FinanceError):
    """Represent invalid user input or invalid persisted data."""


class PersistenceError(FinanceError):
    """Represent a failed load or save operation."""


class ExportError(FinanceError):
    """Represent a failed CSV export."""