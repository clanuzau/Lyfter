
"""
Ejercicio Phyton Basico - Print 2 list at the same time
Student: Cesar Lanuza Urbina
"""

def main():

# List 1
    first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
# List 2
    second_list = ['casos', 'los', 'la', 'por', 'es', 'util']
    
    # Variable initialization
    index = 0
    final_phrase = ""

    print()
    print("Data:")
    print()
    while index < min(len(first_list), len(second_list)):
        final_phrase += first_list[index] + ' ' + second_list[index] + ' '
        print(f"{first_list[index]} {second_list[index]}")
        index += 1
    
    print()
    print("Phrase:")
    print(final_phrase)
    print()

if __name__ == "__main__":
    main()