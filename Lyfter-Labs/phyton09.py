"""
Ejercicio # 6 - Python Basic - Numero mayor
Student: Cesar Lanuza Urbina
"""
def main():
# Operations

    number1  = int(input('Ingrese primer numer      : '))     
    number2  = int(input('Ingrese segundo numero    : '))   
    number3  = int(input('Ingrese tercer numero     : '))
    if number1 > number2 and number1 > number3:
        print(" ")
        print(f"El numero mayor es : {number1}")
    elif number2 > number1 and number2 > number3:
        print(" ")
        print(f"El numero mayor es : {number2}")
    elif number3 > number1 and number3 > number2:
        print(" ")
        print(f"El numero mayor es : {number3}")
    else:
        print(" ")
        print("Los numeros son iguales")
    

if __name__ == "__main__":
    main()