"""
Ejercicio # 5 - Python Basic -Sumas de distintos tipos
Student: Cesar Lanuza Urbina
"""
def main():
# Operations

    string1 = "Hola "
    string2 = "Mundo"
    full_string = string1 + string2
    print(full_string) 
    
    string1 = "Hola "
    int1 = 2026
    full_string = string1 + int1
    print(full_string)  

    string1 = "Hola "
    int1 = 2026
    full_string = int1 + string1
    print(full_string)  

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]   
    full_list = list1 + list2
    print(full_list)    

    string1 = "Hola "
    list1 = [1, 2, 3]   
    full_string = string1 + list1
    print(full_string)  

    float1 = 3.14
    int1 = 2026 
    full_float = float1 + int1
    print(full_float)       

    bool1 = True
    bool2 = False
    full_bool = bool1 + bool2
    print(full_bool)    
    

if __name__ == "__main__":
    main()
