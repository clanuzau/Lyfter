"""
Task Python Básico - Sum all numbers and return the total.
Student: Cesar Lanuza Urbina
"""
# function to sum all numbers in a list
def sum_numbers(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def main():
    numbers = [4, 6, 2, 29] # List of numbers to sum
    result = sum_numbers(numbers)

    print(f"{numbers} -> {result}")



if __name__ == "__main__":
    main()
