"""
Task: Phyton Basico - Convert valid elements to float, add them and print the total.
Student: Cesar Lanuza Urbina
"""


def sum_values(lista):
    
    total = 0.0

    print()
    # Go through every element received in the list.
    for element in lista:
        try:
            # Try to convert the current element to a decimal number.
            value = float(element)

            # Add the converted value to the accumulated total.
            total += value
            print(f"{value} sumado correctamente")
        except (ValueError, TypeError):
            # Report elements that cannot be converted without stopping the loop.
            print(f"Elemento inválido: {element}")

    print()
    print("--- Suma de valores convertibles a float ---")
    print(f"      Total de la suma: {total}")
    print()
    return total


def main():
    my_list = ["10", "manzana", "5.5", "3", "n/a", "7.2", "banana", "2.8"]
    # Call the function sumar_valores to sum the values in the list and print the total.
    sum_values(my_list)


if __name__ == "__main__":
    main()
