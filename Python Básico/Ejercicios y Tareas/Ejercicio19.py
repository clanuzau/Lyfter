"""
Task Python Básico - Reverse String value
Student: Cesar Lanuza Urbina
"""

def swap_string(my_string):
    reversed_string = ""

    for index in range(len(my_string) - 1, -1, -1):
        reversed_string += my_string[index]

    return reversed_string


def main():
    my_string = "Hola mundo"
    new_string = swap_string(my_string)
    print()
    print(f"{my_string} -> {new_string}")
    print()


if __name__ == "__main__":
    main()
