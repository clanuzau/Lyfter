"""
Program: Read a file line by line and save its content in a single line.
Student: Cesar Lanuza Urbina
"""

import os

# Read the lines and remove only their newline characters.
def read_lines(input_file):
     
    with open(input_file, "r", encoding="utf-8") as file:
        return [line.rstrip("\r\n") for line in file]

# Join the lines using a space as the separator.
def join_lines(lines):
     
    return " ".join(lines) # Join the lines into a single string with spaces in between.

# Write the complete text without adding a newline character.
def write_text(output_file, text):
    # encoding="utf-8" is used to ensure that the text is written correctly, 
    # especially if it contains special characters like "!!!""
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

# Coordinate the reading, transformation, and writing process.
def Main():
     
    # Build the paths based on the location of this program.
    current_folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_folder, "LineFeed.txt")
    output_file = os.path.join(current_folder, "Mywords.txt")

    try:
        # Run each stage of the process in order.
        lines = read_lines(input_file)
        text = join_lines(lines)
        write_text(output_file, text)

        print()
        print(f'El contenido fue guardado en "{os.path.basename(output_file)}".')
    except FileNotFoundError:
        print(f'Error: No se encontró el archivo "{os.path.basename(input_file)}".')
    except PermissionError:
        print("Error: No hay permisos para leer o escribir el archivo.")
    except OSError as error:
        print(f"Error mientras se procesaban los archivos: {error}")


if __name__ == "__main__":
    Main()
