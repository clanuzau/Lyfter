"""
Ejercicio Phyton Basico - Print even numbers from a numeric list
Student: Cesar Lanuza Urbina
"""

def main():

# String 

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Keep a copy of the original list to do a comparison at the end
    original_list = my_list.copy()
    
    index =0
    for index, number in enumerate(my_list):
        result = number /2
        if result != 0:
            my_list.pop(index)
    
    print()
    print('---------------------------------------')
    print(f"All numbers : {original_list}")
    print(f"Even numbers: {my_list}")
    print('---------------------------------------')
    print()

if __name__ == "__main__":
    main()