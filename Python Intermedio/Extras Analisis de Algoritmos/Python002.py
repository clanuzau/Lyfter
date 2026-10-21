# Student: Cesar Lanuza Urbina
# Program: Search for a target with linear_search and binary_search, compare
# their complexity and use cases, and demonstrate the effect of unsorted data.


def linear_search(my_list, target):
    """Return whether target exists by checking items in any list order."""
    # Stop as soon as a matching item is found.
    for item in my_list:
        if item == target:
            return True
    return False


def binary_search(my_list, target):
    """Return whether target exists in a list sorted in ascending order."""
    low = 0
    high = len(my_list) - 1
    # Keep an inclusive search interval and discard half on each iteration.
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def main():
    """Demonstrate both searches and explain their requirements and costs."""
    # Use ordered data so both algorithms meet their input requirements.
    ordered_list = [1, 3, 5, 7, 9, 11, 13]
    print(f"Lista ordenada: {ordered_list}")
    # Show both a successful search and an unsuccessful search.
    for target in (7, 8):
        linear_result = linear_search(ordered_list, target)  
        binary_result = binary_search(ordered_list, target)
        print(f"\nElemento buscado: {target}")
        print("Búsqueda lineal: " + ("Encontrado" if linear_result else "No encontrado"))
        print("Búsqueda binaria: " + ("Encontrado" if binary_result else "No encontrado"))

    # Assume constant-time comparisons and indexing for the complexity analysis.
    print("\n1. ¿Cuál es la complejidad de cada algoritmo?")
    print("n representa la cantidad de elementos de la lista. "
          "Se suponen comparaciones y acceso por índice de costo constante.")
    print("Búsqueda lineal: mejor caso O(1), si el primer elemento coincide; "
          "caso promedio y peor caso O(n), porque puede recorrer toda la lista.")
    print("Búsqueda binaria: mejor caso O(1), si el elemento central coincide; "
          "caso promedio y peor caso O(log n), porque reduce el intervalo "
          "de búsqueda aproximadamente a la mitad en cada paso.")
    print("Ambas implementaciones usan espacio auxiliar O(1).")

    print("\n2. ¿En qué condiciones conviene usar cada uno?")
    print("La búsqueda lineal conviene con listas pequeñas, desordenadas o "
          "cuando se realizan pocas búsquedas y no compensa ordenar los datos.")
    print("La búsqueda binaria conviene con listas grandes ya ordenadas "
          "de menor a mayor, especialmente si se realizan muchas búsquedas. "
          "Necesita acceso eficiente por índice y elementos comparables.")
    print("Ordenar primero cuesta O(n log n) en el caso general. Ese costo "
          "puede compensarse al reutilizar la lista ordenada en muchas búsquedas; "
          "no está incluido en el O(log n) de la búsqueda binaria.")

    print("\n3. ¿Qué pasa si la lista no está ordenada?")
    print("La búsqueda lineal sigue funcionando correctamente. La búsqueda "
          "binaria pierde su garantía de corrección: puede descartar la parte "
          "que contiene el elemento y devolver que no existe aunque esté presente.")

    # Deliberately violate the binary search precondition to show a false negative.
    unordered_list = [3, 1, 2]
    target = 3
    print(f"\nEjemplo con lista desordenada: {unordered_list}; elemento buscado: {target}")
    print("Búsqueda lineal: " +
          ("Encontrado" if linear_search(unordered_list, target) else "No encontrado"))
    print("Búsqueda binaria: " +
          ("Encontrado" if binary_search(unordered_list, target) else "No encontrado"))
    print("El resultado binario es incorrecto en este ejemplo: el 3 sí está en la lista.")

    # Sort a copy explicitly so the preparation cost is separate from the search.
    sorted_list = sorted(unordered_list)
    print(f"Lista después de ordenar una copia: {sorted_list}")
    print("Búsqueda binaria con la lista ordenada: " +
          ("Encontrado" if binary_search(sorted_list, target) else "No encontrado"))


# Run the demonstration only when the file is executed directly.
if __name__ == "__main__":
    main()
