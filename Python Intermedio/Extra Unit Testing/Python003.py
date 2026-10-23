"""
Student: Cesar Lanuza Urbina
Program: Read file lines with read_lines and verify the expected contents
and missing-file behavior using pytest, unittest.mock, and the AAA pattern.
Tests simulate file access without creating real input files and print
Spanish success or failure messages after each test execution.
"""

from functools import wraps
from unittest.mock import mock_open, patch

import pytest


# The report_test_result decorator wraps test functions to print their outcomes in Spanish while preserving pytest's failure 
# reporting. It captures exceptions and prints whether the test case passed or failed, including any keyword arguments for clarity.
def report_test_result(test_function):
    """Print the test outcome while preserving pytest failure reporting."""
    @wraps(test_function)
    def wrapper(*args, **kwargs):
        try:
            result = test_function(*args, **kwargs)
        except (Exception, pytest.fail.Exception):
            # Re-raise failures, including missing expected exceptions.
            print(f"Caso de prueba {test_function.__name__}: FALLIDO. La validación no fue exitosa.")
            raise
        else:
            print(f"Caso de prueba {test_function.__name__}: EXITOSO. La validación fue exitosa.")
            return result

    return wrapper


# The read_lines function reads all lines from a specified file and returns them as a list, preserving their original 
# line endings. It raises a FileNotFoundError if the file does not exist.
def read_lines(path):
    """Return all file lines, preserving their original line endings."""
    with open(path, 'r') as f:
        return f.readlines()


# The following test verifies that read_lines correctly returns the expected lines from a simulated file without 
# creating an actual input file. It uses unittest.mock to mock the open function and provide predefined content.
@report_test_result
def test_read_lines_mocked_file_content_tc001():
    """Verify simulated file contents without creating a real input file."""
    # Arrange
    path = "archivo_simulado.txt"
    content = "Primera línea\nSegunda línea\nÚltima línea"
    expected = ["Primera línea\n", "Segunda línea\n", "Última línea"]
    mocked_open = mock_open(read_data=content)

    # Act
    # Replace builtins.open only during the call to prevent real file access.
    with patch("builtins.open", mocked_open):
        result = read_lines(path)

    # Assert
    assert result == expected
    mocked_open.assert_called_once_with(path, 'r')
    mocked_open.return_value.readlines.assert_called_once_with()


# The following test verifies that attempting to read a non-existent file raises a FileNotFoundError with the expected Spanish 
# message. It uses unittest.mock to simulate the missing file scenario without relying on the actual filesystem.
@report_test_result
def test_read_lines_missing_file_tc002():
    """Verify that a simulated missing file propagates FileNotFoundError."""
    # Arrange
    path = "archivo_inexistente.txt"
    expected_message = "El archivo solicitado no existe."
    missing_file_error = FileNotFoundError(expected_message)

    # Act
    # Simulate the failure so the test does not depend on the real filesystem.
    with patch("builtins.open", side_effect=missing_file_error) as mocked_open:
        with pytest.raises(FileNotFoundError) as error:
            read_lines(path)

    # Assert
    assert error.type is FileNotFoundError
    assert str(error.value) == expected_message
    mocked_open.assert_called_once_with(path, 'r')


if __name__ == "__main__":
    # Run pytest directly and display the Spanish outcome of each test.
    raise SystemExit(pytest.main([__file__, "-q", "-s", "-p", "no:cacheprovider"]))