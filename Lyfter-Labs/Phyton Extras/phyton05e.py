"""
Ejercicio Extra - Python Basic - Temperatura
Student: Cesar Lanuza Urbina
"""

def main():
    # Variable inizialization
    temp_celcius    = 0
    temp_farenheit  = 0
    temp_kelvin     = 0
    
    temp_celcius = float(input("Enter celcius temperature: "))

    # Formula to convert from Celcius to Farenheit
    
    temp_farenheit = (temp_celcius * 9/5) + 32

    # Formula to convert from Celcius to Kelvin

    temp_kelvin =  temp_celcius + 273.15 
   
    print()
    print(f"1 Farenheit: {temp_farenheit:.2f}")
    print(f"2 Kelvin: {temp_kelvin:.2f}")   
    print()



if __name__ == "__main__":
    main()
