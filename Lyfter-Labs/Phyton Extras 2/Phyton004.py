"""
Ejercicio Phyton Basico - Print even numbers from a numeric list
Student: Cesar Lanuza Urbina
"""

def main():

# String 

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
    even_list = []
    
    # Keep a copy of the original list to do a comparison at the end
    original_list = my_list.copy()
    
    # % 2 : calculates the remainder after division by 2
    # ==0 : check whether that remainder is zero (even number)
    for number in my_list:
        if number % 2 == 0:
            even_list.append(number)
    
    print()
    print('-------------------------------------------------------------------------------------')
    print(f"All numbers : {original_list}")
    print(f"Even numbers: {even_list}")
    print('-------------------------------------------------------------------------------------')
    print()

if __name__ == "__main__":
    main()
