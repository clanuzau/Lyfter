"""
Ejercicio Extra - Python Basic - Numero 30
Student: Cesar Lanuza Urbina
"""

def main():
    # Variable inizialization
    number1 = 0
    number2 = 0
    number3 = 0
    
    number1 = float(input("Enter number 1: "))
    number2 = float(input("Enter number 2: "))
    number3 = float(input("Enter number 3: "))

    if number1 == 30 or number2 == 30 or number3 == 30:
        print()
        print(f"{number1:.0f},{number2:.0f},{number3:.0f} -> Correcto (hay un 30)")
        print()
    elif number1 + number2 + number3 == 30:
        print()
        print(f"{number1:.0f},{number2:.0f},{number3:.0f} -> Correcto ( {number1:.0f} + {number2:.0f} + {number3:.0f} = 30 )")
        print()
    else : print(f"{number1:.0f},{number2:.0f},{number3:.0f} -> Inorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)")
    print()
       



if __name__ == "__main__":
    main()
