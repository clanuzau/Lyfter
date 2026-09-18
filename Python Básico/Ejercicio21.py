"""
Task Python Básico - Sort words in a string alphabetically.
Student: Cesar Lanuza Urbina
"""

def sort_words(text):
    # Read the string and create a list without using split().
    word_list = []
    current_word = ""

    for character in text:
        if character == "-":
            word_list.append(current_word)
            current_word = ""
        else:
            current_word += character

    word_list.append(current_word)

    # Create a new list and sort the words alphabetically.
    sorted_word_list = word_list[:]

    # Sort the words alphabetically  
    for current_position in range(len(sorted_word_list)):
        for next_position in range(
            current_position + 1, len(sorted_word_list)
        ):
            if sorted_word_list[current_position] > sorted_word_list[next_position]:
                temporary_word = sorted_word_list[current_position]
                sorted_word_list[current_position] = sorted_word_list[next_position]
                sorted_word_list[next_position] = temporary_word

    # Create a new string.
    new_string = ""

    for position in range(len(sorted_word_list)):
        new_string += sorted_word_list[position]

        if position < len(sorted_word_list) - 1:
            new_string += "-"

    return new_string


def main():
    text = "python-variable-funcion-computadora-monitor"
    print()
    new_text = sort_words(text)
    print(f"Original text: {text}")
    print()
    print(f"Sorted text: {new_text}")
    print()

if __name__ == "__main__":
    main()
