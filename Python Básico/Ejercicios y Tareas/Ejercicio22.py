"""
Task Python Básico - List all prime numbers from a list of numbers.
Student: Cesar Lanuza Urbina
"""

# Function to validate if a number is prime.
def is_prime(number):
    if number <= 1:
        return False

    # Check for divisors from 2 through half of the number.
    for divisor in range(2, (number // 2) + 1):
        if number % divisor == 0:
            return False

    return True


def main():
    my_numbers = [1, 4, 6, 7, 13, 9, 67] # input list of numbers
    new_list = []

    for number in my_numbers:
        if is_prime(number):            # validate if the number is prime and add it to the new list
            new_list.append(number)

    print()
    print(f" From {my_numbers} list, prime numbers are: -> {new_list}")
    print()


if __name__ == "__main__":
    main()
