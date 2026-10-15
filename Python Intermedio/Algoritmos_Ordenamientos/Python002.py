"""
Student: Cesar Lanuza Urbina
Program: Bubble Sort Algorithm with Ascending and Descending Order
"""

# This implementation of the Bubble Sort algorithm sorts a list of numbers in ascending or descending order based on the 'reverse'
# parameter. 
def bubble_sort(numbers, reverse=False):
    """Return a sorted copy, using descending order when reverse is True."""
    # Copy the input list to preserve the original numbers and their order.
    numbers = numbers.copy()

    # Each pass moves the largest or smallest remaining number to the end.
    for end in range(len(numbers) - 1, 0, -1):
        swapped = False

        # Compare adjacent numbers in the unsorted portion of the list.
        for index in range(end):
            # Choose the comparison according to the requested sort order.
            if (not reverse and numbers[index] > numbers[index + 1]) or (
                reverse and numbers[index] < numbers[index + 1]
            ):
                # Swap adjacent numbers when they are in the wrong order.
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                swapped = True

        # Stop early if no swaps occurred because the list is already sorted.
        if not swapped:
            break

    return numbers


# Example usage:
if __name__ == "__main__":
    # Run the example only when this file is executed directly.
    numbers = [8, 15, 45, 125, 0, -1, -5, 21, 9]

    # Create both sorted lists without modifying the original list.

    # Sort in ascending order
    ascending_numbers = bubble_sort(numbers)
    # Sort in descending order
    descending_numbers = bubble_sort(numbers, reverse=True)

    print()
    print("Numeros originales", numbers)
    print("Numeros de Menor a Mayor =", ascending_numbers)
    print("Numeros de Mayor a Menor =", descending_numbers)
    print()
