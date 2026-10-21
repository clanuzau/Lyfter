# Student: Cesar Lanuza Urbina
# Program: Calculate the sum of integers from 1 to n using manual_add and
# add_formula, and compare their time and auxiliary space complexity.


def manual_add(n):
    """Sum integers from 1 to n iteratively; n must be a nonnegative integer."""
    result = 0
    # Visit every integer in the inclusive range from 1 to n.
    for i in range(1, n + 1):
        result += i
    return result


def add_formula(n):
    """Sum integers from 1 to n algebraically; n must be a nonnegative integer."""
    # Use integer division to keep the result exact without floating-point rounding.
    return n * (n + 1) // 2


def main():
    """Demonstrate both functions and explain their algorithmic complexity."""
    # Compare both implementations on a small input to avoid a lengthy loop.
    number = 10
    print()
    print(f"Suma de los enteros desde 1 hasta {number}:")
    print(f"Versión 1 (suma manual): {manual_add(number)}")
    print(f"Versión 2 (fórmula): {add_formula(number)}")
    print()

    # Apply the conventional model in which each arithmetic operation costs O(1).
    print("Comparación de complejidad de tiempo y espacio auxiliar:")

    print("\nAnálisis y comparación (modelo de operaciones aritméticas constantes):")
    print("Versión 1: tiempo O(n), porque realiza n iteraciones; espacio auxiliar O(1).")
    print("Versión 2: tiempo O(1), porque realiza una cantidad fija de operaciones; "
          "espacio auxiliar O(1).")
    print("Ambas versiones producen el mismo resultado para enteros no negativos.")
    print("Nota: Python usa enteros de precisión arbitraria. Para números de tamaño "
          "creciente, el costo de las operaciones y la memoria también dependen "
          "de la cantidad de bits; O(1) supone operaciones de costo constante.")

    # Calculate the large example only with the formula to avoid a billion iterations.
    number = 1_000_000_000
    print()
    print("Cual version usar para un número grande (1 000 000 000)?")
    print("\nPara number = 1 000 000 000 usaría la versión 2 (fórmula).")
    print("Evita mil millones de iteraciones y calcula la suma exacta con unas "
          "pocas operaciones aritméticas.")
    print(f"Resultado: {add_formula(number)}")
    print()


# Run the demonstration only when this file is executed directly.
if __name__ == "__main__":
    main()
