"""
Student: Cesar Lanuza Urbina
Program: Perform list and string operations and verify them with pytest.
Main functions: sum_numbers, reverse_string, print_case_counts,
sort_hyphenated_words, and filter_prime_numbers.
Each function has one test case following the Arrange, Act, Assert pattern.
"""

from contextlib import nullcontext
from functools import wraps
from math import isqrt

import pytest


def report_test_result(test_function):
    """Print the test outcome and preserve pytest assertion failures."""
    @wraps(test_function)
    # The wrapper function captures the test result and prints a message indicating success or failure.
    def wrapper(*args, **kwargs):
        message = "FALLIDO. La validación no fue exitosa."
        try:
            result = test_function(*args, **kwargs)
            message = "EXITOSO. La validación fue exitosa."
            return result
        finally:
            # Make the result visible even when the test uses capsys.
            capture = kwargs.get("capsys")
            with capture.disabled() if capture is not None else nullcontext():
                print(f"Caso de prueba {test_function.__name__}: {message}")

    return wrapper


# Main functions for list and string operations.
def sum_numbers(numbers):
    """Return the sum of all numbers in a list."""
    return sum(numbers)

def reverse_string(text):
    """Return a string with its characters in reverse order."""
    return text[::-1]


def print_case_counts(text):
    """Print uppercase and lowercase character counts in Spanish."""
    # Unicode-aware checks include accented letters and ignore spaces.
    uppercase_count = sum(character.isupper() for character in text)
    lowercase_count = sum(character.islower() for character in text)
    print(f"Hay {uppercase_count} mayúsculas y {lowercase_count} minúsculas.")


def sort_hyphenated_words(text):
    """Sort hyphen-separated words alphabetically and rejoin them."""
    # Convert the string into a list, sort it, and rebuild the string.
    words = text.split("-")
    words.sort()
    return "-".join(words)


def filter_prime_numbers(numbers):
    """Return prime integers from a list, preserving order and duplicates."""
    primes = []
    for number in numbers:
        # Prime numbers are integers greater than one.
        if number < 2:
            continue
        # A composite number has a divisor no greater than its square root.
        for divisor in range(2, isqrt(number) + 1):
            if number % divisor == 0:
                break
        else:
            # The loop's else branch runs only when no divisor was found.
            primes.append(number)
    return primes


# Test cases for the main functions using pytest.
@report_test_result
def test_sum_numbers_list_sum_tc001():
    """Verify that all values in the example list contribute to the sum."""
    # Arrange
    numbers = [4, 6, 2, 29]
    expected = 41

    # Act
    result = sum_numbers(numbers)

    # Assert
    assert result == expected


# Test case for reversing a string while preserving spaces and characters.
@report_test_result
def test_reverse_string_character_order_tc002():
    """Verify that reversing a string preserves its spaces and characters."""
    # Arrange
    text = "Hola mundo"
    expected = "odnum aloH"

    # Act
    result = reverse_string(text)

    # Assert
    assert result == expected


# Test case for counting uppercase and lowercase letters in a string.
@report_test_result
def test_print_case_counts_uppercase_and_lowercase_tc003(capsys):
    """Use pytest's capsys fixture to verify the printed Spanish message."""
    # Arrange
    text = "I love Nación Sushi"
    expected = "Hay 3 mayúsculas y 13 minúsculas.\n"

    # Act
    print_case_counts(text)
    captured = capsys.readouterr()

    # Assert
    # The example contains 13 lowercase letters, including the accented ó.
    assert captured.out == expected


#   Test case for sorting hyphen-separated words alphabetically.
@report_test_result
def test_sort_hyphenated_words_alphabetical_order_tc004():
    """Verify alphabetical ordering and preservation of hyphen separators."""
    # Arrange
    text = "python-variable-funcion-computadora-monitor"
    expected = "computadora-funcion-monitor-python-variable"

    # Act
    result = sort_hyphenated_words(text)

    # Assert
    assert result == expected

# Test case for filtering prime numbers from a list of integers.
@report_test_result
def test_filter_prime_numbers_prime_selection_tc005():
    """Verify that one and composite numbers are excluded from the result."""
    # Arrange
    numbers = [1, 4, 6, 7, 13, 9, 67]
    expected = [7, 13, 67]

    # Act
    result = filter_prime_numbers(numbers)

    # Assert
    assert result == expected


if __name__ == "__main__":
    # Run pytest when this file is executed directly and display test messages.
    raise SystemExit(pytest.main([__file__, "-q", "-s", "-p", "no:cacheprovider"]))