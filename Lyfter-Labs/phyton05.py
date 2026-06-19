"""
Ejercicio # 5 - Python Basic - Calcular Edad 
Student: Cesar Lanuza Urbina
"""
def main():
# Calcular edad
    NAME    = str(input('Ingrese Nombre    : '))
    SURNAME = str(input('Ingrese Apellidos : '))
    AGE    = int(input('Ingrese Edad      : ')) 

    if AGE <= 1:
        print(" ")
        print(f"{NAME} es un bebé")
    elif AGE <= 6: 
        print(" ")
        print(f"{NAME} es un niña")   
    elif AGE <= 12: 
        print(" ")
        print(f"{NAME} es un preadolescente")   
    elif AGE <= 20: 
        print(" ")
        print(f"{NAME} es un adolescente")   
    elif AGE <= 25: 
        print(" ")
        print(f"{NAME} es adulto joven")   
    elif AGE <= 60: 
        print(" ")
        print(f"{NAME} es un adulto")   
    elif AGE > 60: 
        print(" ")
        print(f"{NAME} es una adulto mayor")   

if __name__ == "__main__":
    main()
