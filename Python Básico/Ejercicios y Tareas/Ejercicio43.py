"""
Student: Cesar Lanuza Urbina
Program: Load existing Pokemon and save a new Pokemon to a JSON file.
"""

import json
import math
from pathlib import Path


# Locate the JSON file next to this script.
FILE_PATH = Path(__file__).resolve().parent / "pokemons.json"

# Function to read existing Pokemon from a JSON file.
def read_pokemons(filename=FILE_PATH):
    """Load existing Pokemon or start an empty list if the file is missing."""
    try:
        with open(filename, "r", encoding="utf-8-sig") as file:
            pokemons = json.load(file) # Load the JSON data from the file.
    except FileNotFoundError:
        return []

    # Reject an unexpected structure before modifying existing data.
    # isinstance(value, type) checks whether a value has the specified type.
    # Here, it checks that pokemons is a list and each Pokemon is a dictionary.
    if not isinstance(pokemons, list) or not all(
        isinstance(pokemon, dict) for pokemon in pokemons
    ):
        raise ValueError("El archivo debe contener una lista de objetos Pokémon.")
    return pokemons


# Function to ask for a required text value.
def ask_text(message):
    """Ask for a required text value."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Este campo no puede estar vacío.")


# Function to ask for an integer level between 1 and 100.
def ask_level():
    """Ask for an integer level between 1 and 100."""
    while True:
        try:
            level = int(input("Nivel (1-100): "))
            if 1 <= level <= 100:
                return level
        except ValueError:
            pass
        print("Ingrese un número entero entre 1 y 100.")


# Function to ask for a positive, finite weight in kilograms.
def ask_weight():
    """Ask for a positive, finite weight in kilograms."""
    while True:
        try:
            weight = float(input("Peso en kg (ej. 6.0): ").replace(",", "."))
            if math.isfinite(weight) and weight > 0:
                return weight
        except ValueError:
            pass
        print("Ingrese un peso válido mayor que cero.")


# Function to ask if the Pokemon is shiny and return a boolean value.
def ask_shiny():
    """Convert the user's answer to a boolean."""
    while True:
        answer = input("¿Es shiny? (sí/no): ").strip().casefold()
        if answer in ("sí", "si", "s", "true"):
            return True
        if answer in ("no", "n", "false"):
            return False
        print("Responda sí o no.")


# Function to collect skill names as a list of strings.
def ask_skills():
    """Collect skill names as a list of strings."""
    while True:
        answer = input("Habilidades -separadas por comas-: ")
        skills = [skill.strip() for skill in answer.split(",") if skill.strip()]
        if skills:
            return skills
        print("Ingrese al menos una habilidad.")


# Function to collect all fields for a new Pokemon and return them as a dictionary.
def ask_pokemon():
    """Collect all fields for the new Pokemon."""
    print("\nIngrese la información del nuevo Pokémon:")
    name = ask_text("Nombre: ")
    pokemon_type = ask_text("Tipo (ej. Electric): ")
    level = ask_level()
    weight = ask_weight()
    is_shiny = ask_shiny()

    # Store an empty held item as None, which becomes null in JSON.
    held_item = input("Objeto equipado (Enter si no tiene): ").strip() or None
    skills = ask_skills()

    return {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
    }


# Function to save the list of Pokemon to a JSON file.
def save_pokemons(pokemons, filename=FILE_PATH):
    """Save the complete Pokemon list as readable JSON."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(pokemons, file, ensure_ascii=False, indent=4)
        file.write("\n")


def main():
    """Read existing records, collect a new Pokemon, and save the list."""
    # Stop on invalid JSON or read errors to protect existing records.
    try:
        pokemons = read_pokemons() # Load existing Pokemon from the JSON file.
    except (OSError, UnicodeError, ValueError) as error:
        print(f"No se pudo leer el archivo de Pokémon: {error}")
        return

    print(f"Pokémon existentes: {len(pokemons)}")
    pokemon = ask_pokemon()

    # Append the new record while keeping all previously loaded Pokemon.
    pokemons.append(pokemon)
    try:
        save_pokemons(pokemons) # Save the updated list back to the JSON file.
    except (OSError, UnicodeError) as error:
        print(f"No se pudo guardar el archivo de Pokémon: {error}")
        return

    print(f"\n{pokemon['name']} se agregó correctamente a {FILE_PATH.name}.")
    print()
    

# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
