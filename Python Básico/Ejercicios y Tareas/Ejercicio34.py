"""
Program: Count the total number of words in a text file.
Student: Cesar Lanuza Urbina
"""

import os

# Read the entire content of the file.
"""Read all the text content from the input file."""
def read_content(input_file):
    # Read the entire content of the file and return it as a string.
    with open(input_file, "r", encoding="utf-8") as file: # Open the input file in read mode with UTF-8 encoding.
        return file.read()   

# Count the words separated by spaces and/or line breaks.
"""Count the words using whitespace as the separator."""
def count_words(content):
    # Count the number of words in the content by splitting it based on whitespace.
    return len(content.split())

# Coordinate the reading and counting process.
"""Run the reading and word-counting process in order."""
def main():
    
    # Build the path based on the location of this program.
    current_folder = os.path.dirname(os.path.abspath(__file__))
    # Build the path to the input file based on the current folder.
    input_file = os.path.join(current_folder, "WordNumbers.txt")

    try:
        content = read_content(input_file) # Read the content of the input file
        total_words = count_words(content) # Count the total number of words in the content

        print()
        print(f'Este archivo contiene "{total_words}" palabras.')
        print()
        print()
        print(content)
    except FileNotFoundError:
        print()
        print(f'Error: No se encontró el archivo "{os.path.basename(input_file)}".')
        print()
    except PermissionError:
        print()
        print("Error: No hay permisos para leer el archivo.")
        print()
    except OSError as error:
        print(f"Error mientras se procesaba el archivo: {error}")


if __name__ == "__main__":
    main()
