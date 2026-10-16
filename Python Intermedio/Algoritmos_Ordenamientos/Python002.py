"""
Student: Cesar Lanuza Urbina
Program: Bubble Sort Algorithm with Right-to-Left Traversal
"""

# Traverse from right to left to move smaller values toward the beginning.
def bubble_sort(numbers):
    """Return an ascending sorted copy using right-to-left Bubble Sort."""
    # Copy the input list to preserve the original numbers and their order.
    numbers = numbers.copy()

    # Each pass places the smallest remaining value at the left boundary.
    for boundary in range(len(numbers) - 1):
        swapped = False

        # Scan backward from the last index to the position after the boundary.
        for index in range(len(numbers) - 1, boundary, -1):
            # Move the current value left when it is smaller than its left neighbor.
            if numbers[index] < numbers[index - 1]:
                numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
                swapped = True

        # Stop early if no swaps occurred because the list is already sorted.
        if not swapped:
            break

    return numbers


# Example usage:
if __name__ == "__main__":
    # Run the example only when this file is executed directly.
    numbers = [8, 15, 45, 125, 0, -1, -5, 21, 9]

    # Sort in ascending order without modifying the original list.
    ascending_numbers = bubble_sort(numbers)

    print()
    print("Números originales:", numbers)
    print("Recorrido de Bubble Sort: de derecha a izquierda.")
    print("Números de menor a mayor:", ascending_numbers)
    print()
