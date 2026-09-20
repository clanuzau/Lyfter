"""
Task: Phyton Basico - Validar que el nombre no sea numerico
Student: Cesar Lanuza Urbina
"""

# Request the user's name and validate that it is not numeric.
def request_name():
    name = input("Ingrese su nombre: ")

    # Validate that the name is not numeric.
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")

    return name

# Request the user's age and convert it to an integer.
def request_age():
    
    return int(input("Ingrese su edad: "))


def main():
    # Added try-except block to handle the ValueError raised by request_name function
    try:
        name = request_name()
    except ValueError as error:
        print(error)
        return

    # Added try-except block to handle the ValueError raised by request_age function
    try:
        age = request_age()
    except ValueError:
        print("Número no valido")
        return

    print(f"Hola {name}, su edad es {age}")


if __name__ == "__main__":
    main()
