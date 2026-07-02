"""
Ejercicio Phyton Basico - Average value from a numeric list
Student: Cesar Lanuza Urbina
"""

def main():

    my_values = [10, 20, 30, 35, 40, 45, 50, 60, 65, 70]
    new_list = []  # This will contain values greater than or equal to the average.

    # Calculate the average value of the list
    average_number = sum(my_values) / len(my_values)

    print()
    print(f"The average number value is: {average_number}")

    print()
    print(f"Original List: {my_values}")
    print()

    for value in my_values:
        if value >= average_number:
            new_list.append(value)
    
    print(f"New List: {new_list}")
    print()
    
if __name__ == "__main__":
    main()