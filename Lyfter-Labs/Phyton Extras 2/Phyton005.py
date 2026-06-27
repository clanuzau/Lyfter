"""
Ejercicio Phyton Basico - Enter 10 numbers and list the higher value
Student: Cesar Lanuza Urbina
"""

def main():

    numbers = []
    counter = 1

    while counter <= 10:
        value = input(f"Enter number {counter} of 10: ")

        try:
            number = int(value)
            numbers.append(number)
            counter += 1
        except ValueError:
            print("Invalid input. Enter number only.")
    
    print()
    print(f"Numbers entered are: {numbers}. The highest value entered was: {max(numbers)}")
    print()
          

if __name__ == "__main__":
    main()