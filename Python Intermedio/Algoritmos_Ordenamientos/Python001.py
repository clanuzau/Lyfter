"""
Student: Cesar Lanuza Urbina
Program: Bubble Sort Algorithm
"""

# This implementation of the Bubble Sort algorithm sorts a list of numbers in ascending order.
# The algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 
# The process is repeated until the list is sorted.


# Bubble Sort Algorithm Implementation in Python
def bubble_sort(numbers):
    # Each pass moves the largest remaining number to the end.
    for end in range(len(numbers) - 1, 0, -1):
        swapped = False

        # Compare adjacent numbers in the unsorted portion of the list.
        for index in range(end):
            if numbers[index] > numbers[index + 1]:
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
    numbers = [50, -6, 2, 10, -4, 88, 5, 25, 35]
    print()
    print("Números originales:", numbers)
    bubble_sort(numbers)
    print("Números ordenados:", numbers)
    print()
