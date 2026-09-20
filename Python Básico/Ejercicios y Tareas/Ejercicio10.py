"""
Ejercicio Phyton Basico - Generate a word list with more than 4 chars
Student: Cesar Lanuza Urbina
"""

def main():

    word_list = []
    new_list = []
    counter = 5

    print()
    for number in range(1, counter + 1):
        my_word = input(f"Enter word # {number}: ")
        word_list.append(my_word)
        if len(my_word) > 4:
            new_list.append(my_word)

    print()
    print(f"My List : {word_list}")
    print(f"Final List: {new_list}")
    print()
    
if __name__ == "__main__":
    main()