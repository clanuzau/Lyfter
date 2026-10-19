"""
Student: Cesar Lanuza Urbina
Program: Validate numeric input before applying Bubble Sort.
"""

from math import isnan


def bubble_sort(numbers):
    """Return an ascending sorted copy using right-to-left Bubble Sort."""
    # Preserve the original list while exchanging adjacent values in the copy.
    numbers = numbers.copy()
    for boundary in range(len(numbers) - 1):
        swapped = False

        # Move the smallest remaining value toward the left boundary.
        for index in range(len(numbers) - 1, boundary, -1):
            if numbers[index] < numbers[index - 1]:
                numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
                swapped = True

        # A pass without swaps means the entire list is already sorted.
        if not swapped:
            break

    return numbers


def validated_bubble_sort(numbers):
    """Validate a nonempty list of integers or floats, then return a sorted copy."""
    if not isinstance(numbers, list):
        raise TypeError("Error: La entrada debe ser una lista")

    if not numbers:
        raise ValueError("Error: La lista no puede estar vacía")

    # Booleans are integer subclasses, but are not accepted as numeric input here.
    for number in numbers:
        if isinstance(number, bool) or not isinstance(number, (int, float)):
            raise TypeError("Error: La lista contiene elementos no numéricos")
        # NaN cannot participate in a meaningful ascending comparison.
        if isinstance(number, float) and isnan(number):
            raise ValueError("Error: La lista contiene un valor NaN que no se puede ordenar")

    # Sort only after every element has passed validation.
    return bubble_sort(numbers)


if __name__ == "__main__":
    # Demonstrate valid input, a nonnumeric element, and an empty list.
    examples = [[5, 3, 1, 2, 4], [5, "hola", 2], []]
    for numbers in examples:
        print("Entrada:", numbers)
        try:
            print("Lista ordenada:", validated_bubble_sort(numbers))
        except (TypeError, ValueError) as error:
            # Display validation errors in Spanish without an unhandled traceback.
            print(error)
        print()
