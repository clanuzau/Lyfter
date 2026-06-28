"""
Ejercicio Phyton Basico - Retrieve and count the same element in a list
Student: Cesar Lanuza Urbina
"""

def main():

# String 

    my_list = [2, 4, 6, 6, 8, 10, 14, 6, 7, 12, 6, 1, 3, 5, 9]
    final_list = []
    
    # Keep a copy of the original list to do a comparison at the end
    original_list = my_list.copy()
    
    print()
    value = int(input("Search for number: "))
    times_found = my_list.count(value)
    if times_found == 0:
        print(f"Number {value} is not in the list")
    else:
        print()
        print(f"Number {value} appears {times_found} times.")
    print()
    
    
if __name__ == "__main__":
    main()