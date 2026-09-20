"""
Student: Cesar Lanuza Urbina
Program: Read Pokemon from a JSON file and display their name, type, and level.
"""

import json
from pathlib import Path

# Function to read and validate the list of Pokemon from the JSON file.
def read_pokemons(filename):
    """Read and validate the list of Pokemon from the JSON file."""
    # Convert the JSON data into Python objects.
    with open(filename, "r", encoding="utf-8-sig") as file:
        pokemons = json.load(file)

    # isinstance checks that the data is a list containing dictionaries.
    
    # isinstance(pokemons, list) checks whether the loaded data is a list.
    # all(...) checks whether every item in that list is a dictionary.
   
    if not isinstance(pokemons, list) or not all(
        isinstance(pokemon, dict) for pokemon in pokemons
    ):
        raise ValueError("El archivo debe contener una lista de objetos Pokémon.")

    return pokemons

# Function to display the list of Pokemon in the console.
def display_pokemons(pokemons):
    """Display each Pokemon's name, type, and level in the console."""
    # Explain when the file contains an empty list.
    if not pokemons:
        print("No hay Pokémon registrados en el archivo.")
        return

    print("Pokémon registrados:\n")

    # Loop through the list and use a fallback for missing attributes.
    for pokemon in pokemons:
        name = pokemon.get("name", "No disponible")
        pokemon_type = pokemon.get("type", "No disponible")
        level = pokemon.get("level", "No disponible")
        print(f"Nombre: {name} | Tipo: {pokemon_type} | Nivel: {level}")
        print()


# Main function to coordinate reading the JSON file and displaying the Pokemon.
def main():
    """Coordinate reading the JSON file and displaying the Pokemon."""
    # Report missing files, invalid JSON, and other reading errors.

    # Locate the JSON file created in the previous exercise next to this script.
    filename = Path(__file__).resolve().parent / "pokemons.json"

    try:
        pokemons = read_pokemons(filename)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {filename}")
        return
    except (OSError, UnicodeError, ValueError) as error:
        print(f"No se pudo leer el archivo de Pokémon: {error}")
        return

    display_pokemons(pokemons)


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
