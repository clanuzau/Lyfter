"""
Ejercicio Phyton Basico - Switch first and last element from a list.
Student: Cesar Lanuza Urbina
"""

def main():

# String 

    my_list = [10, 4, 3, 6, 1, 7, 5]
    
    # Keep a copy of the original list to do a comparison at the end
    original_list = my_list.copy()
    
    # Retrive the first and last position from the list
    init_value = my_list[0]
    last_value = my_list[len(my_list)-1]

    # Replace the first position of the list with the last value (last_value) and
    # last position of the list with first value (init_value)

    my_list[0] = last_value
    my_list[-1] = init_value
    
    print()
    print('---------------------------------------')
    print(f"Original List: {original_list}")
    print(f"Result: {my_list}")
    print('---------------------------------------')
    print()

if __name__ == "__main__":
    main()