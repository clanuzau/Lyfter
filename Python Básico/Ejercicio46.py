"""
Student: Cesar Lanuza Urbina
Program: Read Pokemon from a JSON file and display their attributes.
Expected fields: name, type, level, weight_kg, is_shiny, held_item, and skills.
"""

import json
from pathlib import Path


# Function to read and validate the list of Pokemon from the JSON file.
def read_pokemons(filename):
    """Read and validate the Pokemon list from a JSON file."""
    # Convert the JSON file contents into Python objects.
    with open(filename, "r", encoding="utf-8-sig") as file:
        pokemons = json.load(file)

    # Check that the loaded data is a list and every item is a dictionary.
    if not isinstance(pokemons, list) or not all(
        isinstance(pokemon, dict) for pokemon in pokemons
    ):
        raise ValueError("El archivo debe contener una lista de objetos Pokémon.")

    return pokemons


# Function to display the attributes of each Pokemon in the console.
def display_statistics(pokemons):
    """Display each Pokemon's name, type, level, weight, shiny status, item, and skills."""
    # Show a message when the JSON file contains an empty list.
    if not pokemons:
        print("No hay Pokémon registrados en el archivo.")
        return

    # Read each Pokemon's attributes from the loaded JSON records.
    for pokemon in pokemons:
        # Convert booleans, null items, and skill lists into readable text.
        is_shiny = pokemon.get("is_shiny")
        shiny_text = "No disponible"
        if isinstance(is_shiny, bool):
            shiny_text = "Sí" if is_shiny else "No"

        held_item = pokemon.get("held_item", "No disponible")
        if held_item is None:
            held_item = "Ninguno"

        skills = pokemon.get("skills")
        skills_text = "No disponible"
        if isinstance(skills, list):
            skills_text = ", ".join(str(skill) for skill in skills) or "Ninguna"

        print()
        # Display each attribute with a fallback for missing values.
        print(f"Nombre: {pokemon.get('name', 'No disponible')}")
        print(f"Tipo: {pokemon.get('type', 'No disponible')}")
        print(f"Nivel: {pokemon.get('level', 'No disponible')}")
        print(f"Peso (kg): {pokemon.get('weight_kg', 'No disponible')}")
        print(f"Es shiny: {shiny_text}")
        print(f"Objeto equipado: {held_item}")
        print(f"Habilidades: {skills_text}")
        print()  # Separate Pokemon with a blank line.


# Main function to coordinate reading the JSON file and displaying the Pokemon.
def main():
    """Load the Pokemon file and display the available attributes."""
    # Locate the JSON file from the previous exercise next to this script.
    filename = Path(__file__).resolve().parent / "pokemons.json"

    # Handle missing files, invalid JSON, and other reading errors.
    try:
        pokemons = read_pokemons(filename)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {filename}")
        return
    except (OSError, UnicodeError, ValueError) as error:
        print(f"No se pudo leer el archivo de Pokémon: {error}")
        return

    display_statistics(pokemons)


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
