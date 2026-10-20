"""
Student: Cesar Lanuza Urbina
Program: Demonstrate and analyze four algorithms using Big O notation.
Main functions: print_numbers_times_2, check_if_lists_have_an_equal,
print_10_or_less_elements, generate_list_trios, and main.

Complexity assumes constant-time arithmetic, equality, and output for
fixed-size elements. List lengths are independent unless stated otherwise.
"""


def print_numbers_times_2(numbers_list):
    """Print doubled numbers: O(n) time and O(1) auxiliary space."""
    # Visit each of the n elements once, performing constant work per element.
    for number in numbers_list:
        print(number * 2)


def check_if_lists_have_an_equal(list_a, list_b):
    """Find a shared element: O(n*m) worst-case time, O(1) extra space."""
    # Each element of list_a may be compared with every element of list_b.
    for element_a in list_a:
        for element_b in list_b:
            # Early return gives O(1) best-case time when the first pair matches.
            if element_a == element_b:
                return True

    return False


def print_10_or_less_elements(list_to_print):
    """Print up to ten elements: O(1) time and O(1) auxiliary space."""
    # Python lists store their length, so len() takes constant time.
    list_len = len(list_to_print)
    # The loop performs at most ten iterations, regardless of input size.
    for index in range(min(list_len, 10)):
        print(list_to_print[index])


def generate_list_trios(list_a, list_b, list_c):
    """Build all trios: O(n*m*p) time and output space for nonempty inputs."""
    result_list = []
    # Three independent loops enumerate the Cartesian product of the lists.
    for element_a in list_a:
        for element_b in list_b:
            for element_c in list_c:
                # String creation is O(1) only for bounded element lengths.
                result_list.append(f'{element_a} {element_b} {element_c}')

    return result_list


def main():
    """Run small examples and explain time and space complexity."""

    print("ANÁLISIS DE ALGORITMOS CON NOTACIÓN BIG O")
    print() 
    print("\n1. Imprimir cada número multiplicado por dos")
    print()
    print_numbers_times_2([1, 2, 3, 4])
    print("n = cantidad de números. Se realizan n iteraciones.")
    print("Tiempo: O(n), tanto en el mejor como en el peor caso.")
    print("Espacio auxiliar: O(1); no se construye una lista adicional.")
    print()

    print("\n2. Comprobar si dos listas tienen un elemento en común")
    print()
    # Translate the Boolean result instead of displaying English literals.
    has_equal = check_if_lists_have_an_equal([1, 2, 3], [4, 3, 5]) # True
    print(f"¿Hay un elemento en común? {'Sí' if has_equal else 'No'}")
    print("n = tamaño de la primera lista; m = tamaño de la segunda.")
    print("Peor caso: O(n*m), con n*m comparaciones si no hay coincidencias.")
    print("Mejor caso: O(1), si el primer par comparado coincide.")
    print("Si ambas listas tienen tamaño n, el peor caso es O(n²).")
    print("Sin una distribución de entradas, no se establece un caso promedio.")
    print("Espacio auxiliar: O(1).")
    print("Si la primera lista está vacía: O(1). Si solo la segunda lo está: O(n).")
    print("Incluyendo listas vacías, la cota general es O(1 + n + n*m).")

    print("\n3. Imprimir diez elementos o menos")
    print()
    print_10_or_less_elements(list(range(1, 13)))
    print("n = tamaño de la lista. Se realizan min(n, 10) iteraciones.")
    print("Tiempo: O(1), porque el número de iteraciones nunca supera diez.")
    print("Espacio auxiliar: O(1).")
    print()

    print("\n4. Generar todas las combinaciones de tríos")
    print()
    trios = generate_list_trios([1, 2], [3, 4], [5, 6])
    print("Tríos generados:")
    for trio in trios:
        print(trio)
    print(f"Cantidad de tríos: {len(trios)}")
    print("n, m y p son los tamaños de las tres listas, respectivamente.")
    print("Con listas no vacías, se generan exactamente n*m*p tríos.")
    print("Tiempo: O(n*m*p). Si las tres listas tienen tamaño n: O(n³).")
    print("Espacio del resultado: O(n*m*p); espacio auxiliar sin resultado: O(1).")
    print("No hay salida anticipada: se recorren todas las combinaciones.")
    print("Si alguna lista está vacía, no se generan tríos, pero pueden ejecutarse ciclos externos.")
    print("Incluyendo listas vacías, el tiempo es O(1 + n + n*m + n*m*p).")
    print("Si cada texto generado tiene hasta L caracteres, su creación cuesta O(L).")
    print("Para listas no vacías, tiempo y espacio del resultado son entonces O(n*m*p*L).")
    print()


if __name__ == "__main__":
    main()
