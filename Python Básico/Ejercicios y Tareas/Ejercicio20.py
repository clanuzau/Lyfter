"""
Task Python Básico - Count uppercase and lowercase letters in a string.
Student: Cesar Lanuza Urbina
"""

# function to count uppercase and lowercase letters in a string
def count_upper_and_lower(my_string):
    upper_cases = 0
    lower_cases = 0

    for character in my_string: # iterate through each character in the string
        if character.isupper():
            upper_cases += 1
        elif character.islower():
            lower_cases += 1

    print()
    print(f"{my_string} -> There's {upper_cases} upper cases and {lower_cases} lower cases")
    print()


def main():
    my_string = "I love Nación Sushi" # string to count uppercase and lowercase letters
    count_upper_and_lower(my_string)  # call the function to count uppercase and lowercase letters


if __name__ == "__main__":
    main()
