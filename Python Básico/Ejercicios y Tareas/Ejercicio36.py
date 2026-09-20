"""
Program: Phyton036.py - Add new lines to a file without erasing the previous content.
Student: Cesar Lanuza Urbina
"""

# Function that asks the user for a line of text and returns it.
def get_line():
    line = input("Ingrese la linea de texto: ")
    return line

# Function that appends the line to the end of the file. If the file does not exist,
# it creates it. The line is written without erasing the previous content.
def append_line_to_file(line, filename="UserText.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(line + "\n")
    print("El texto se agrega al final del archivo sin borrar lo anterior.")

# Function that asks the user if they want to add another line.
# Returns True if the answer is S/SI/SÍ, and False otherwise.
def wants_new_line():
    answer = input("Desea agregar nueva linea? [S/N]: ").strip().upper()
    return answer in ("S", "SI", "SÍ")

# Main function that coordinates the process of adding new lines to the file.
def main():
    print()
    print("=== AGREGAR LINEAS AL ARCHIVO UserText.txt ===")
    while True:
        line = get_line()  # Asks the user for a line of text.
        append_line_to_file(line)  # Appends the line to the end of the file.
        if not wants_new_line():  # Asks if the user wants to add another line.
            break
    print()
    print("Programa finalizado.")
    print()


if __name__ == "__main__":
    main()
