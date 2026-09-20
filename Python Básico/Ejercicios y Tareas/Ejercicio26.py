"""
Task: Phyton Basico - Minimum words in a string
Student: Cesar Lanuza Urbina
"""

def filter_words(words, n):
    """Return the words that contain more than n letters."""
    filtered_words = []

    # Check each word in the original list.
    for word in words:
        # Keep only words with more than n letters.
        if len(word) > n:
            # Add qualifying words to the new filtered list.
            filtered_words.append(word)

    return filtered_words


def main():

    words = ["Rojo", "Amarillo", "Azul", "Verde", "Naranja", "Morado", "Rosa", "Negro", "Blanco", "Gris"]
    print()
    n = int(input("Ingrese el número de letras: "))
    print()

    result = filter_words(words, n)
    print(f"Palabras con más de {n} letras: {result}")
    print()

if __name__ == "__main__":
    main()

