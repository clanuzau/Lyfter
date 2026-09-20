"""
Student: Cesar Lanuza Urbina
Program: Group Pokemon by type and display the average level of each type.
"""

import json
from pathlib import Path


def read_pokemons(filename):
    """Read and validate the Pokemon records from a JSON file."""
    # Convert the JSON file contents into Python objects.
    with open(filename, "r", encoding="utf-8-sig") as file:
        pokemons = json.load(file)

    # Require a list of dictionaries before processing the records.
    if not isinstance(pokemons, list) or not all(
        isinstance(pokemon, dict) for pokemon in pokemons
    ):
        raise ValueError("El archivo debe contener una lista de objetos Pokémon.")

    # Validate the fields needed to group Pokemon and calculate averages.
    for position, pokemon in enumerate(pokemons, start=1):
        pokemon_type = pokemon.get("type")
        level = pokemon.get("level")

        if not isinstance(pokemon_type, str) or not pokemon_type.strip():
            raise ValueError(f"El Pokémon #{position} debe tener un tipo válido.")
        
        if isinstance(level, bool) or not isinstance(level, int) or level < 1:
            raise ValueError(
                f"El Pokémon #{position} debe tener un nivel entero mayor que cero."
            )

    return pokemons


# Group Pokemon by type and calculate the average level for each type.
def group_by_type(pokemons):
    """Return a dictionary containing a list of Pokemon for each type."""
    groups = {}

    for pokemon in pokemons:
        # Ignore surrounding spaces and capitalization when grouping types.
        pokemon_type = pokemon["type"].strip().casefold()
        if pokemon_type not in groups:
            groups[pokemon_type] = []
        groups[pokemon_type].append(pokemon)

    return groups


# Calculate the average level for each Pokemon type.
def calculate_average_levels(groups):
    """Calculate the average level for each Pokemon type."""
    averages = {}

    # Divide the sum of levels by the number of Pokemon in each group.
    for pokemon_type, pokemons in groups.items():
        total_level = sum(pokemon["level"] for pokemon in pokemons)
        averages[pokemon_type] = total_level / len(pokemons)

    return averages


# Display the average level for each Pokemon type.
def display_averages(averages):
    """Display each type and its average level with one decimal place."""
    # Handle an empty Pokemon list without attempting any division.
    if not averages:
        print("No hay Pokémon registrados en el archivo.")
        return

    print()
    for pokemon_type, average in averages.items():
        print(f"Tipo: {pokemon_type.capitalize()} → Promedio de nivel: {average:.1f}")

    print()  # Add a blank line after the averages for better readability.


# Main function to read Pokemon, group them by type, and display their average levels.
def main():
    """Read Pokemon, group them by type, and display their average levels."""
    # Locate the JSON file from the previous exercise next to this script.
    filename = Path(__file__).resolve().parent / "pokemons.json"

    # Report missing files, invalid JSON, and invalid Pokemon records.
    try:
        pokemons = read_pokemons(filename)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {filename}")
        return
    except (OSError, UnicodeError, ValueError) as error:
        print(f"No se pudo leer el archivo de Pokémon: {error}")
        return

    groups = group_by_type(pokemons)
    averages = calculate_average_levels(groups)
    display_averages(averages)


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
