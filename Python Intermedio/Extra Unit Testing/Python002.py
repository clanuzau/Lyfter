"""
Student: Cesar Lanuza Urbina
Program: Divide two numbers with divide and verify normal division,
zero division, and string inputs using pytest and the AAA pattern.
Each test execution prints its outcome in Spanish.
"""

from functools import wraps

import pytest


# The report_test_result decorator wraps test functions to print their outcomes in Spanish while preserving pytest's failure 
# reporting. It captures exceptions and prints whether the test case passed or failed, including any keyword arguments for clarity.
def report_test_result(test_function):
    """Print the outcome without suppressing pytest assertion failures."""
    @wraps(test_function)
    def wrapper(*args, **kwargs):
        case_name = test_function.__name__
        # Identify each string-input variant in the printed result.
        if kwargs:
            case_name += f" ({kwargs!r})"
        try:
            result = test_function(*args, **kwargs)
        except (Exception, pytest.fail.Exception):
            # Preserve the original failure so pytest reports it correctly.
            print(f"Caso de prueba {case_name}: FALLIDO. La validación no fue exitosa.")
            raise
        else:
            print(f"Caso de prueba {case_name}: EXITOSO. La validación fue exitosa.")
            return result

    return wrapper


# The divide function performs division of two numbers, raising a ValueError for division by zero.
def divide(number1, number2):
    """Return the quotient, rejecting division by zero with ValueError."""
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2


# The following test verifies that dividing two valid numbers returns the expected float result.
@report_test_result
def test_divide_valid_numbers_tc001():
    """Verify that dividing 10 by 2 returns the float 5.0."""
    # Arrange
    number1, number2 = 10, 2
    expected = 5.0

    # Act
    result = divide(number1, number2)

    # Assert
    assert result == expected
    assert isinstance(result, float)


# The following test verifies that dividing by zero raises a ValueError with the expected Spanish message.
@report_test_result
def test_divide_zero_denominator_tc002():
    """Verify the exception type and Spanish message for division by zero."""
    # Arrange
    number1, number2 = 10, 0
    expected_message = "No se puede dividir por cero"

    # Act
    # pytest.raises captures ValueError and fails if it is not raised.
    with pytest.raises(ValueError) as error:
        divide(number1, number2)

    # Assert
    assert str(error.value) == expected_message


# The following test uses pytest's parameterization to check that passing a string in either parameter raises a TypeError.
@pytest.mark.parametrize("number1, number2", [("10", 2), (10, "2")])
# The test_divide_string_parameter_tc003 function verifies that a TypeError is raised when a string is passed as either parameter.
@report_test_result
def test_divide_string_parameter_tc003(number1, number2):
    """Verify that a string in either parameter raises TypeError."""
    # Arrange
    expected_exception = TypeError

    # Act
    # Capture the expected exception without relying on its system message.
    with pytest.raises(expected_exception) as error:
        divide(number1, number2)

    # Assert
    assert error.type is expected_exception


if __name__ == "__main__":
    # Run pytest directly and disable output capture to display each outcome.
    raise SystemExit(pytest.main([__file__, "-q", "-s", "-p", "no:cacheprovider"]))