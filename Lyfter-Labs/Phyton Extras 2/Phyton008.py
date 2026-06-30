"""
Ejercicio Phyton Basico - Minimum value in the list
Student: Cesar Lanuza Urbina
"""

def main():

# String : Numbers including negative values

    my_values = [15, -4, 32, 0, -10, 25, 54, -200]

    minimum_value = my_values[0]

    for value in my_values[1:]:
        if value < minimum_value:
            minimum_value = value

    print()
    print(f"The minimum value is: {minimum_value}")
    print()
    
if __name__ == "__main__":
    main()