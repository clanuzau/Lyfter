"""
Task Python Básico - Variable Scope
Student: Cesar Lanuza Urbina
"""

message = "Valor global original"


def print_first_message():
    """Print the first message and call the second function."""
    local_message = "Esta variable solo existe dentro de la primera funcion"

    print("Este mensaje se imprime desde la primera funcion.")
    print_second_message()

    # The local variable can be used inside the function.
    print(f"Variable local dentro de la funcion: {local_message}")


def print_second_message():
    """Print a different message from the first function's message."""
    print("Este mensaje se imprime desde la segunda funcion.")


def change_global_message():
    """Access the global variable and change its value."""
    global message

    print(f"Variable global leida desde la funcion: {message}")
    message = "Valor global modificado desde una funcion"


print_first_message()

# Attempt to access a function's local variable from outside the function.
try:
    print(local_message)
except NameError:
    print("No se puede acceder a 'local_message' fuera de su funcion.")

print(f"Variable global antes del cambio: {message}")
change_global_message()
print(f"Variable global despues del cambio: {message}")

