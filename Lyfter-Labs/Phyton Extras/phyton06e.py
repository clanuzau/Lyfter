"""
Ejercicio Extra - Python Basic - Tabla de Multiplicar.
Student: Cesar Lanuza Urbina
"""

def main():
    # Variable inizialization
    mynumber = 0
    
    while True:
        user_input = input("Enter a valid number between 1-10: ").strip()

        if not user_input.isdigit():
            print()
            print("Enter a valid number")
            continue

        mynumber = int(user_input)

        if 1 <= mynumber <= 10:
            break

        print("Enter a number between 1 and 10")

    for counter in range(1, 13):
        total = mynumber * counter
        print(f"{mynumber} x {counter} = {total}")


if __name__ == "__main__":
    main()
