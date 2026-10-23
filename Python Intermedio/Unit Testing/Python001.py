"""
Student: Cesar Lanuza Urbina
Program: Sort lists with bubble_sort and validate its behavior using pytest.
Main functions: bubble_sort and four AAA test cases covering small lists,
large lists, empty lists, and invalid input types.
"""

from functools import wraps

import pytest


def report_test_result(test_function):
    """Print each test outcome while preserving pytest failure reporting."""
    @wraps(test_function)
    def wrapper(*args, **kwargs):
        case_name = test_function.__name__
        # Include parameter values to distinguish parametrized executions.
        if args or kwargs:
            case_name += f" ({args!r}, {kwargs!r})"
        try:
            result = test_function(*args, **kwargs)
        except (Exception, pytest.fail.Exception):
            # Re-raise so a failed assertion or missing exception still fails.
            print(f"Caso de prueba {case_name}: FALLIDO. La validación no fue exitosa.")
            raise
        else:
            print(f"Caso de prueba {case_name}: EXITOSO. La validación fue exitosa.")
            return result

    return wrapper


def bubble_sort(values):
    """Sort a list in ascending order in place and return the same list."""
    # Reject unsupported containers before attempting to sort their elements.
    if not isinstance(values, list):
        raise TypeError("El parámetro debe ser una lista.")

    # Each pass moves the largest remaining element to its final position.
    for end in range(len(values) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swapped = True
        # Stop early when a complete pass makes no changes.
        if not swapped: 
            break

    return values


# Test case for a small list with negative numbers and duplicate values, which should return a sorted list.
@report_test_result
def test_bubble_sort_small_list_tc001():
    """Verify a small list with negative numbers and duplicate values."""
    # Arrange
    values = [5, -2, 3, 0, 3, 1]
    expected = [-2, 0, 1, 3, 3, 5]

    # Act
    result = bubble_sort(values)

    # Assert
    assert result == expected


# Test case for a large list of 150 elements, which should return a sorted list from 1 to 150.
@report_test_result
def test_bubble_sort_large_list_tc002():
    """Verify a descending list containing more than 100 elements."""
    # Arrange
    values = list(range(150, 0, -1))
    expected = list(range(1, 151))

    # Act
    result = bubble_sort(values)

    # Assert
    assert result == expected # Test case for a large list of 150 elements, which should return a sorted list from 1 to 150.


# Test case for an empty list, which should return an empty list.
@report_test_result
def test_bubble_sort_empty_list_tc003():
    """Verify that an empty list produces an empty result."""
    # Arrange
    values = []
    expected = []

    # Act
    result = bubble_sort(values)

    # Assert
    # Verify that the result is an empty list, as expected.
    assert result == expected


# Test case for invalid input types, which should raise a TypeError with a Spanish message.
@pytest.mark.parametrize("invalid_value", [None, 42, 3.14, True, "321", (3, 2, 1), {3, 2, 1}, {"a": 1}])
@report_test_result
def test_bubble_sort_non_list_input_tc004(invalid_value):
    """Verify that non-list parameters raise TypeError with a Spanish message."""
    # Arrange
    expected_message = "El parámetro debe ser una lista."

    # Act
    # pytest.raises captures the expected exception and fails if none is raised.
    with pytest.raises(TypeError) as error:
        bubble_sort(invalid_value)

    # Assert
    # Verify that the exception message matches the expected Spanish message.
    assert str(error.value) == expected_message
