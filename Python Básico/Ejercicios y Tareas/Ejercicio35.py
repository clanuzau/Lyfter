"""
Program: Read a file line by line, convert each line to uppercase, and write it to a new file.
Student: Cesar Lanuza Urbina
"""

import os

# Read the file line by line and return the lines as a list.
"""Read the lines from the input file and return them as a list of strings."""
def read_lines(input_file):
    # Open the input file in read mode with UTF-8 encoding.
    with open(input_file, "r", encoding="utf-8") as file:
        # Read all the lines from the file, keeping each line as a separate element.
        return [line for line in file]

# Convert each line to uppercase.
"""Convert each line of the list to uppercase."""
def to_uppercase(lines):
    # Create a new list with each line converted to uppercase.
    return [line.upper() for line in lines]

# Write the lines to a new file.
"""Write the list of lines to the output file."""
def write_lines(output_file, lines):
    # Open the output file in write mode with UTF-8 encoding.
    with open(output_file, "w", encoding="utf-8") as file:
        # Write each line to the file, preserving the line breaks.
        for line in lines:
            file.write(line)

# Coordinate the reading, uppercase conversion, and writing process.
"""Run the reading, uppercase conversion, and writing process in order."""
def main():
    
    # Build the path based on the location of this program.
    current_folder = os.path.dirname(os.path.abspath(__file__))
    # Build the path to the input file based on the current folder.
    input_file = os.path.join(current_folder, "MyReadingFile.txt")
    # Build the path to the output file based on the current folder.
    output_file = os.path.join(current_folder, "ReadingFile.txt")

    try:
        # Run each stage of the process in order.
        lines = read_lines(input_file) # Read the file line by line.
        upper_lines = to_uppercase(lines) # Convert each line to uppercase.
        write_lines(output_file, upper_lines) # Write the result to the new file.

        print()
        print(f'El contenido fue guardado en "{os.path.basename(output_file)}".')
        print()
        print()
        # Read the content of the output file and print it to the console.
        with open(output_file, "r", encoding="utf-8") as file:
            output_content = file.read()
        print(output_content) # Print the content of the output file to the console.
        print()
    except FileNotFoundError:
        print()
        print(f'Error: No se encontró el archivo "{os.path.basename(input_file)}".')
        print()
    except PermissionError:
        print()
        print("Error: No hay permisos para leer o escribir el archivo.")
        print()
    except OSError as error:
        print(f"Error mientras se procesaban los archivos: {error}")


if __name__ == "__main__":
    main()
