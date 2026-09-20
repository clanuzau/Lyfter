"""
Task: Phyton Basico - Convert valid string elements to integers and report invalid values
Student: Cesar Lanuza Urbina
"""

# Function to convert valid string elements to integers and report invalid values.
def convertir_a_entero(lista):
    # Store only the elements that are successfully converted to integers.
    converted_numbers = []

    # Try to convert each element without stopping the remaining conversions.
    for element in lista:
        try:
            # Convert the current string element to an integer.
            converted_element = int(element)

            # Add the converted integer to the result list.
            converted_numbers.append(converted_element)
            print(f"{element} convertido a {converted_element}")
        except ValueError:
            # Report an invalid element and continue with the next one.
            print(f"No se pudo convertir el elemento: {element}")

    # Return all the elements that were successfully converted.
    return converted_numbers


def main():
    # Define a list of strings to convert to integers.
    my_list = ["4", "hola", "10", "5.2", "mundo", "7", "3.14", "8"]

    print("Resultado:")
    convertir_a_entero(my_list)


if __name__ == "__main__":
    main()
