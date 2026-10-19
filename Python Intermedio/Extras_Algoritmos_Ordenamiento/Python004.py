"""
Student: Cesar Lanuza Urbina
Program: Right-to-left Bubble Sort with pass and swap counters.
"""


# Define a function to perform Bubble Sort from right to left, counting passes and swaps.
def bubble_sort_steps(numbers):
    """Return an ascending sorted copy, the number of passes, and total swaps."""
    # Preserve the input list so callers can reuse its original order.
    numbers = numbers.copy()
    iterations = 0
    swaps = 0

    # Count complete outer passes, not individual adjacent comparisons.
    # Perform all n - 1 passes; empty and single-element lists need none.
    for boundary in range(len(numbers) - 1):
        iterations += 1

        # Scan from right to left, placing the smallest remaining value at the boundary.
        for index in range(len(numbers) - 1, boundary, -1):
            if numbers[index] < numbers[index - 1]:
                # Exchange adjacent values and count each actual swap once.
                numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
                swaps += 1

    return numbers, iterations, swaps


if __name__ == "__main__":
    # This example requires four passes and six adjacent swaps.
    numbers = [5, 3, 1, 2, 4, 8, 7, 6]
    # Call the function to sort the list and retrieve the sorted result along with counts.
    sorted_numbers, iterations, swaps = bubble_sort_steps(numbers) 

    print()
    print("Lista original:", numbers)
    print()
    print("Lista ordenada:", sorted_numbers)
    print("Iteraciones:", iterations)
    print("Intercambios:", swaps)
    print()
