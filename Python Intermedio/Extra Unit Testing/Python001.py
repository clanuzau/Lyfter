"""
Student: Cesar Lanuza Urbina
Program: Add numbers, calculate averages, and convert Celsius to Fahrenheit.
NumericOperations provides three numeric operations. TestNumericOperations
verifies each operation with positive, negative, and zero inputs using pytest
and the Arrange, Act, Assert pattern.
"""

from functools import wraps

import pytest


def report_test_result(test_function):
    """Print a Spanish outcome while preserving pytest failure reporting."""
    @wraps(test_function)
    def wrapper(*args, **kwargs):
        try:
            result = test_function(*args, **kwargs)
        except (Exception, pytest.fail.Exception):
            # Re-raise the original error so pytest still marks the case failed.
            print(f"Caso de prueba {test_function.__name__}: FALLIDO. La validación no fue exitosa.")
            raise
        else:
            print(f"Caso de prueba {test_function.__name__}: EXITOSO. La validación fue exitosa.")
            return result

    return wrapper


# The NumericOperations class provides three independent numeric operations: addition, average calculation, 
# and Celsius to Fahrenheit conversion. Each method is static, allowing them to be called without creating 
# an instance of the class.
class NumericOperations:
    """Provide three independent numeric operations."""

    # The add_numbers method returns the sum of two numbers.
    @staticmethod
    def add_numbers(first, second):
        """Return the sum of two numbers."""
        return first + second

    # The calculate_average method computes the arithmetic mean of a nonempty list of numbers.
    @staticmethod
    def calculate_average(numbers):
        """Return the arithmetic mean of a nonempty list of numbers."""
        if not numbers:
            raise ValueError("La lista debe contener al menos un número.")
        return sum(numbers) / len(numbers)

    # The celsius_to_fahrenheit method converts a Celsius temperature to Fahrenheit using the formula F = C * 9/5 + 32.
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert a Celsius temperature to Fahrenheit."""
        return celsius * 9 / 5 + 32


# The TestNumericOperations class contains unit tests for the NumericOperations class. Each test method is decorated
# with report_test_result to provide Spanish output indicating whether the test passed or failed. 
# The tests cover positive, negative, and zero inputs for all three operations.
class TestNumericOperations:
    """Cover positive, negative, and zero inputs for all three operations."""

    # Each test method follows the Arrange, Act, Assert pattern and is decorated with report_test_result to provide Spanish output.
    @report_test_result
    def test_add_numbers_positive_numbers_tc001(self):
        """Verify addition with two positive numbers."""
        # Arrange
        first, second = 4, 6
        expected = 10

        # Act
        result = NumericOperations.add_numbers(first, second)

        # Assert
        assert result == expected

    # Each test method follows the Arrange, Act, Assert pattern and is decorated with report_test_result to provide Spanish output.
    @report_test_result
    def test_add_numbers_negative_numbers_tc002(self):
        """Verify addition with two negative numbers."""
        # Arrange
        first, second = -4, -6
        expected = -10

        # Act
        result = NumericOperations.add_numbers(first, second)

        # Assert
        assert result == expected

    # Each test method follows the Arrange, Act, Assert pattern and is decorated with report_test_result to provide Spanish output.
    @report_test_result
    def test_add_numbers_zeros_tc003(self):
        """Verify that adding two zeros produces zero."""
        # Arrange
        first, second = 0, 0
        expected = 0

        # Act
        result = NumericOperations.add_numbers(first, second)

        # Assert
        assert result == expected

    # Each test method follows the Arrange, Act, Assert pattern and is decorated with report_test_result to provide Spanish output.
    @report_test_result
    def test_calculate_average_positive_numbers_tc004(self):
        """Verify the mean of positive numbers with a fractional result."""
        # Arrange
        numbers = [2, 3, 5]
        expected = 10 / 3

        # Act
        result = NumericOperations.calculate_average(numbers)

        # Assert
        # Approximate comparisons account for floating-point precision.
        assert result == pytest.approx(expected)

    # Each test method follows the Arrange, Act, Assert pattern and is decorated with report_test_result to provide Spanish output.
    @report_test_result
    def test_calculate_average_negative_numbers_tc005(self):
        """Verify the mean of negative numbers with a fractional result."""
        # Arrange
        numbers = [-2, -3, -5]
        expected = -10 / 3

        # Act
        result = NumericOperations.calculate_average(numbers)

        # Assert
        assert result == pytest.approx(expected)

    # Each test method follows the Arrange, Act, Assert pattern and is decorated with report_test_result to provide Spanish output.
    @report_test_result
    def test_calculate_average_zeros_tc006(self):
        """Verify that a nonempty list of zeros has a zero mean."""
        # Arrange
        numbers = [0, 0, 0]
        expected = 0

        # Act
        result = NumericOperations.calculate_average(numbers)

        # Assert
        assert result == pytest.approx(expected)

    # Each test method follows the Arrange, Act, Assert pattern and is decorated with report_test_result to provide Spanish output.
    @report_test_result
    def test_celsius_to_fahrenheit_positive_number_tc007(self):
        """Verify conversion of a positive Celsius temperature."""
        # Arrange
        celsius = 25
        expected = 77

        # Act
        result = NumericOperations.celsius_to_fahrenheit(celsius)

        # Assert
        assert result == pytest.approx(expected)

    # Each test method follows the Arrange, Act, Assert pattern and is decorated with report_test_result to provide Spanish output.
    @report_test_result
    def test_celsius_to_fahrenheit_negative_number_tc008(self):
        """Verify conversion of a negative Celsius temperature."""
        # Arrange
        celsius = -10
        expected = 14

        # Act
        result = NumericOperations.celsius_to_fahrenheit(celsius)

        # Assert
        assert result == pytest.approx(expected)

    # Each test method follows the Arrange, Act, Assert pattern and is decorated with report_test_result to provide Spanish output.
    @report_test_result
    def test_celsius_to_fahrenheit_zero_tc009(self):
        """Verify that zero Celsius corresponds to 32 Fahrenheit."""
        # Arrange
        celsius = 0
        expected = 32

        # Act
        result = NumericOperations.celsius_to_fahrenheit(celsius)

        # Assert
        assert result == pytest.approx(expected)


if __name__ == "__main__":
    # Allow direct execution while delegating test discovery to pytest.
    raise SystemExit(pytest.main([__file__, "-q", "-s", "-p", "no:cacheprovider"]))