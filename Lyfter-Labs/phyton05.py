"""
Ejercicio # 5 - Python Basic - Calcular Edad 
Student: Cesar Lanuza Urbina
"""
def main():
# Calcular edad
    NAME    = str(input('Ingrese Nombre    : '))
    SURNAME = str(input('Ingrese Apellidos : '))
    EDAD    = int(input('Ingrese Edad      : ')) 

    if EDAD <= 1:
        print(" ")
        print(f"{NAME} es una bebé")
    if EDAD > 1 and EDAD <= 6: 
        print(" ")
        print(f"{NAME} es una niña")   
    if EDAD > 6 and EDAD <= 12: 
        print(" ")
        print(f"{NAME} es una preadolescente")   
    if EDAD > 12 and EDAD <= 20: 
        print(" ")
        print(f"{NAME} es una adolescente")   
    if EDAD > 20 and EDAD <= 25: 
        print(" ")
        print(f"{NAME} es adulta joven")   
    if EDAD > 25 and EDAD <= 60: 
        print(" ")
        print(f"{NAME} es un adulta")   
    if EDAD > 60: 
        print(" ")
        print(f"{NAME} es una adulta mayor")   

if __name__ == "__main__":
    main()
