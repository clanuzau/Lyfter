"""
Task: Phyton Basico - Return the number of vowels contained in a string.
Student: Cesar Lanuza Urbina
"""


def count_vowels(my_text):
    
    vowels_qty = 0

    # Convert the text to lowercase and examine each character.
    for letter in my_text.lower():
        # Check whether the current character is a vowel.
        if letter in "aeiou":
            # Increase the counter when a vowel is found.
            vowels_qty += 1

    return vowels_qty


def main():

    print()
    my_text = input("Ingrese un texto: ")
    print()
    vowels_qty = count_vowels(my_text)
    print(f"El texto contiene {vowels_qty} vocales")
    print()

if __name__ == "__main__":
    main()

