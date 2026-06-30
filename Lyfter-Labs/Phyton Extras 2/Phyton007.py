"""
Ejercicio Phyton Basico - Retrieve negative value in a list
Student: Cesar Lanuza Urbina
"""

def main():

# String : Numbers including negative values

    my_numbers = [2, 4, 8, 10, 14, 6, 7, 12, 1, 3, 5, 9, 0, -2]
    negative_numbers = []
    counter = 0

    # look in my number, for every value
    for number in my_numbers:
        if number <= 0:                          # is a negative one
            negative_numbers.append(number)     # add this negative to negative_number list.
            counter +=1     
    
    print()
    if counter == 1:
        print(f"Hay al menos {counter} numero negativo o cero")
    else:
        print(f"Hay al menos {counter} numeros negativos o cero")
    print()
    
if __name__ == "__main__":
    main()
