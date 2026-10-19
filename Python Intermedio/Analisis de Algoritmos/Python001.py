"""
Student: Cesar Lanuza Urbina
Program: Analyze optimized Bubble Sort through operation counts and Big O notation.
"""

from random import Random


# The Bubble Sort algorithm repeatedly steps through the list, compares adjacent elements, 
# and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, 
# which means the list is sorted. This implementation includes an optimization that stops the algorithm 
# if no swaps occur during a pass, indicating that the list is already sorted.       


def bubble_sort(values):
    """Sort a list in place and return comparison and swap counts."""
    comparisons = 0
    swaps = 0

    # Each pass places the largest remaining element at the end: O(n) passes.
    for end in range(len(values) - 1, 0, -1):
        swapped = False

        # Compare adjacent elements in the unsorted section: O(n) per pass.
        for index in range(end):
            comparisons += 1
            if values[index] > values[index + 1]:
                # A comparison and a swap of numeric elements take O(1) time.
                values[index], values[index + 1] = values[index + 1], values[index]
                swaps += 1
                swapped = True

        # An already sorted list needs just one pass, giving an O(n) best case.
        if not swapped:
            break

    # Only a fixed number of auxiliary variables is used: O(1) extra space.
    return comparisons, swaps


# Demonstration functions below are not part of the algorithm and are not counted in Big O analysis.
def analyze_case(name, values):
    """Display operation counts for one input without modifying the original."""
    # This demonstration copy uses O(n) space; it is not part of Bubble Sort.

    ordered_values = values.copy() # Copy the list to avoid modifying the original.
    comparisons, swaps = bubble_sort(ordered_values) # Count operations on the copy.

    print(f"\nCaso: {name}")
    print(f"Lista original: {values}")
    print(f"Lista ordenada: {ordered_values}")
    print(f"Comparaciones: {comparisons}")
    print(f"Intercambios: {swaps}")


# Compare best-case and worst-case counts as input size doubles.
def show_growth():
    """Compare exact best-case and worst-case counts as input size doubles."""
    print("\nCrecimiento de las comparaciones al duplicar el tamaño:")
    print(f"{'Tamaño':>8} | {'Mejor caso':>12} | {'Peor caso':>12}")
    # Theoretical best case: n - 1 comparisons, worst case: n(n - 1)/2 comparisons.
    for size in (10, 20, 40, 80, 160):
        ascending = list(range(size)) # Create a sorted list for the best case.
        descending = list(range(size, 0, -1))  # Create a reverse-sorted list for the worst case.
        best_comparisons, _ = bubble_sort(ascending) # Count comparisons for the best case.
        worst_comparisons, _ = bubble_sort(descending) # Count comparisons for the worst case.
        
        print(f"{size:>8} | {best_comparisons:>12} | {worst_comparisons:>12}")


# Main function to demonstrate the algorithm and explain its asymptotic complexity.
def main():
    """Demonstrate the algorithm and explain its asymptotic complexity."""
    print("ANÁLISIS DE BUBBLE SORT CON NOTACIÓN BIG O")
    print("Se utiliza una versión con salida anticipada si no hay intercambios.")

    # A fixed seed makes this random example reproducible across runs.
    random_values = list(range(1, 9))
    Random(42).shuffle(random_values)
    analyze_case("mejor caso: lista ordenada", list(range(1, 9)))
    analyze_case("ejemplo de lista desordenada", random_values)
    analyze_case("peor caso: orden inverso", list(range(8, 0, -1)))
    show_growth()

    # Theoretical analysis of the algorithm's time and space complexity.
    print("\nANÁLISIS TEÓRICO")
    print("n representa la cantidad de elementos de la lista.")
    print("Mejor caso: O(n). Para n >= 2, se realizan n - 1 comparaciones.")
    print("Caso promedio: O(n²), suponiendo permutaciones igualmente probables.")
    print("Peor caso: O(n²), cuando los elementos distintos están en orden inverso.")
    print("En el peor caso: (n - 1) + (n - 2) + ... + 1 = n(n - 1)/2.")
    print("Se omiten constantes y términos menores: (n² - n)/2 crece como n².")
    print("Al duplicar n, el peor caso requiere aproximadamente cuatro veces más comparaciones.")
    print("Espacio auxiliar del algoritmo: O(1), porque ordena la lista en su lugar.")
    print("La copia utilizada para mostrar cada ejemplo requiere O(n) espacio adicional.")
    print("Las listas vacías o de un elemento requieren cero comparaciones: O(1).")
    print("Sin salida anticipada, esta estructura de ciclos sería O(n²) incluso en el mejor caso.")
    print("Big O expresa una cota superior de crecimiento, no un tiempo exacto en segundos.")
    print("Los ejemplos ilustran el análisis; una lista aleatoria no demuestra el caso promedio.")


if __name__ == "__main__":
    main()
