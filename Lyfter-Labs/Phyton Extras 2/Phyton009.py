"""
Ejercicio Phyton Basico - Average value from a numeric list
Student: Cesar Lanuza Urbina
"""

def main():

    # Imnport from statistics the function/method mean
    from statistics import mean

    my_values = [10, 20, 30, 35, 40, 45, 50, 60, 65, 70]
    new_list = [] # This will contain the values higher than average from the list

    average_number = mean(my_values) # get the average from the list value

    print()
    print(f"The average number value is: {average_number}")

    for value in my_values[1:]: # read and get the values in the list
        if value >= average_number:
            new_list.append(value) # If condition is true, add the number to the new list.
    
    print(f"New List: {new_list}")
    print()
    
if __name__ == "__main__":
    main()