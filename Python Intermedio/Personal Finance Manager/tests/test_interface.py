"""
Student: Cesar Lanuza Urbina
Program: Verify the Spanish error dialog against the actual FreeSimpleGUI popup signature.
"""

from unittest.mock import patch

from finance_manager.errors import ValidationError
from finance_manager.interface import show_error


def test_show_error_spanish_button_tc033():
    """Use autospec to reject unsupported popup arguments without opening a GUI."""
    # Arrange
    error = ValidationError("Seleccione una categoría existente.")
    with patch("finance_manager.interface.sg.popup", autospec=True) as popup:
        # Act
        show_error(error)

    # Assert
    popup.assert_called_once_with(
        "Seleccione una categoría existente.",
        title="No se pudo completar la operación",
        custom_text=("Aceptar", None),
        keep_on_top=True,
    )