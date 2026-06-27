"""
Ejercicio Phyton Basico - Letter strings
Student: Cesar Lanuza Urbina
"""

def main():

# String 

    my_string = 'Pizza con piña'

    # range(start, stop, step)
        # start = len(my_string) - 1 : index of the last character.
        # stop =  -1 : stop before reaching -1, so index 0 is included.
        # step = 1 : decrease the index by one each iteration.

    print()
    
    for index in range(len(my_string) - 1, -1, -1):
        print(my_string[index])
    
    print()

if __name__ == "__main__":
    main()