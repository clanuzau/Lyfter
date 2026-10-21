# Student: Cesar Lanuza Urbina
# Program: Print every ordered pair of dictionary keys with print_all_pairs,
# analyze its time complexity, and estimate the runtime for one million keys.


def print_all_pairs(my_dict):
    """Print all ordered pairs of keys, including each key paired with itself."""
    # For each outer key, visit every key again in the inner loop.
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")


def main():
    """Demonstrate the function and explain its quadratic output growth."""
    # Keep the demonstration small because the function prints n squared lines.
    sample_dict = {"uno": 1, "dos": 2, "tres": 3}
    print("Pares de claves de un diccionario con 3 claves:")
    print_all_pairs(sample_dict)
    print(f"Total de pares impresos: {len(sample_dict) ** 2}")

    print("\n¿Cuál es la complejidad temporal?")
    print()
    print("Sea n la cantidad de claves. El ciclo externo se ejecuta n veces "
          "y el interno recorre n claves por cada iteración externa.")
    print("Se realizan exactamente n × n = n² impresiones: la complejidad "
          "temporal es Θ(n²), y por lo tanto también O(n²), suponiendo un "
          "costo constante por impresión.")
    print("Se incluyen los pares de una clave consigo misma y ambos órdenes "
          "de cada par; no hay una salida anticipada.")
    print("Si la longitud de las claves varía, convertirlas a texto y escribir "
          "sus caracteres también influye en el tiempo. La salida puede "
          "dominar el costo real del programa.")

    # Estimate the output count without constructing or printing the huge input.
    key_count = 1_000_000
    pair_count = key_count ** 2
    print("\n¿Cuánto dura si hay 1 millón de claves?")
    print()
    print("Con 1 000 000 de claves se generan 1 000 000 000 000 pares "
          "(un billón de impresiones).")
    print("No se puede determinar una duración exacta solo con la complejidad. "
          "Depende del equipo, la longitud de las claves y si la salida va "
          "a una terminal o a un archivo.")
    print("Tiempo estimado en segundos = cantidad de pares / pares impresos "
          "por segundo.")

    # Use an explicitly hypothetical sustained rate, not a measured benchmark.
    assumed_pairs_per_second = 1_000_000
    estimated_seconds = pair_count / assumed_pairs_per_second
    estimated_days = estimated_seconds / (24 * 60 * 60)
    seconds_text = f"{estimated_seconds:,.0f}".replace(",", " ")
    days_text = f"{estimated_days:.2f}".replace(".", ",")
    print("Ejemplo hipotético: si se lograra imprimir 1 000 000 de pares "
          "por segundo de manera sostenida:")
    print(f"Duración estimada: {seconds_text} segundos, "
          f"aproximadamente {days_text} días.")
    print("Esta velocidad es una suposición, no una medición. Una salida "
          "más lenta aumentaría el tiempo proporcionalmente.")
    print("El ejemplo de un millón de claves se calcula sin imprimir sus pares "
          "para evitar una ejecución extremadamente larga.")


# Run the demonstration only when this file is executed directly.
if __name__ == "__main__":
    main()
