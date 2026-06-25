"""
Ejercicio Extra - Python Basic - Tiempo en segundos
Student: Cesar Lanuza Urbina
"""
import random

def main():
    # Variable inizialization
    time_in_minutes = 0
    remaining_seconds = 0

    seconds = float(input("Enter seconds: "))
    
    time_in_minutes = seconds / 60

    if time_in_minutes < 10:
        remaining_seconds = 600 - seconds 
        print(f"Segundos faltantes para los 10 minutos : {remaining_seconds:.0f}")
    elif time_in_minutes > 10:
        remaining_seconds = seconds - 600
        print(f"Mayor")
    else:
        print(" ")
        print("El tiempo ingresado es exactamente 10 minutos")  
    

if __name__ == "__main__":
    main()
