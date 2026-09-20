"""
Task: Phyton Basico - Find and count a character in a string 
Student: Cesar Lanuza Urbina
"""
# Function count_chars
def count_chars(my_text, char_acter):
    count_letters = 0

    
    for letter in my_text: 
        if letter == char_acter:
            count_letters += 1

    return count_letters


def main():

    print()
    my_text = input("Ingrese un texto: ")
    print()
    char_acter  = input("Ingrese el carácter que desea buscar: ")

    chars_qty  = count_chars(my_text, char_acter)
    print()
    print(f"Se ha encontrado {chars_qty} veces el carácter")
    print()


if __name__ == "__main__":
    main()
