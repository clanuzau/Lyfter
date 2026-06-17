"""
Ejercicio # 6 - Python Basic - Adivinar numero secreto entre 1 y 10
Student: Cesar Lanuza Urbina
"""
import random

def main():
    # Generar un numero secreto entre 1 y 10
    random_number = random.randint(1, 10)
    my_number = int(input("Ingrese numero: "))

    while my_number != random_number:
        print(" ")
        print("Lo siento, intente de nuevo")
        my_number = int(input("Ingrese numero: "))

    print(" ")
    print(f"Correcto, el numero secreto es: {random_number}")


if __name__ == "__main__":
    main()
