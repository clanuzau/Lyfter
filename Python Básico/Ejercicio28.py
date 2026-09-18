"""
Task: Phyton Basico - Arithmetic Operations
Student: Cesar Lanuza Urbina
"""

# Show the menu of available operations and the current result.
def show_menu(current_number):
    """Show the current result and the available operations."""
    print()
    print(f"Resultado actual: {current_number}")
    print()
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado")
    print("6. Finalizar")


# Request an operand and return None when its value is invalid.
def request_number():
    
    user_input = input("Ingrese un numero: ")

    try:
        return float(user_input)
    except ValueError:
        print("Error: debe ingresar un numero valido.")
        return None


# Perform an arithmetic operation using the accumulated result.
# Return the result of applying the selected operation.
def calculate(current_number, new_number, option):
     
    if option == "1":
        return current_number + new_number
    if option == "2":
        return current_number - new_number
    if option == "3":
        return current_number * new_number

    return current_number / new_number


# Ask whether the user wants to perform another operation.
def request_continue():
    while True:
        print()
        answer = input("Desea continuar [S/N]? ").strip()

        if answer in ("S", "s", "N", "n"):
            return answer in ("S", "s")

        print("Error: ingrese solamente S o N.")


# Main function that runs the calculator program.
def main():
    current_number = 0.0

    # Loop to continuously show the menu and perform operations until the user decides to exit. 
    while True:
        show_menu(current_number)
        print()
        option = input("Seleccione una opcion: ").strip()

        if option not in ("1", "2", "3", "4", "5", "6"):
            print("Error: la opcion seleccionada no es valida.")
            continue

        if option == "5":
            current_number = 0.0
            print("El resultado fue borrado.")
            continue

        if option == "6":
            break

        # Request one new number to operate on the accumulated result.
        new_number = None
        while new_number is None:
            new_number = request_number()

        # Zero is not a valid divisor. Request the number again.
        while option == "4" and new_number == 0:
            print("Error: no se puede dividir entre cero.")
            new_number = None
            while new_number is None:
                new_number = request_number()

        current_number = calculate(current_number, new_number, option)

        print(f"Resultado: {current_number}")

        # Ask the user if they want to continue with another operation or exit the program.
        if not request_continue():
            break

    print()
    print("Programa finalizado.")
    print()


if __name__ == "__main__":
    main()
