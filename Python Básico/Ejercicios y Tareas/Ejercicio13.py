"""
Ejercicio Phyton Basico - Delete keys and values from a dictionary using a list 
Student: Cesar Lanuza Urbina
"""

def main():

    # Define a list of keys to be used in the dictionary
    list_of_keys = ['access_level', 'age']

     # Define a dictionary with some key-value pairs
    employee = {'name': 'John', 
                'email': 'john@ecorp.com', 
                'access_level': 5, 
                'age': 28
     }
 
    print()
    print(f"Original Dictionary: {employee}")
    print()

    # Delete the specified keys from the dictionary using a loop (for)
    for key in list_of_keys:
        employee.pop(key)

    print()
    print(f"Dictionary after deleting keys {list_of_keys}: {employee}")
    print()
    print(employee)
    print()    

if __name__ == "__main__":
    main()
