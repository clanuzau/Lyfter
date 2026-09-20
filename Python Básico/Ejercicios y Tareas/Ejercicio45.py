"""
Student: Cesar Lanuza Urbina
Program: Find Pokemon by type from a JSON file.
"""

import json
from pathlib import Path


# Read and validate the Pokemon list from the JSON file.
def read_pokemons(filename):
	"""Return the Pokemon records stored in a JSON file."""
	with open(filename, "r", encoding="utf-8-sig") as file:
		pokemons = json.load(file)

    # isinstance checks that the data is a list containing dictionaries.
	if not isinstance(pokemons, list) or not all(
		isinstance(pokemon, dict) for pokemon in pokemons
	):
		raise ValueError("El archivo debe contener una lista de objetos Pokémon.")

	return pokemons


# Ask the user for the Pokemon type to search for.
def ask_pokemon_type():
	"""Return a non-empty Pokemon type entered by the user."""
	while True:
		pokemon_type = input(
			"Ingrese el tipo de Pokémon que desea buscar "
			"(agua, electrico, fuego, etc.): "
		).strip()
		if pokemon_type:
			return pokemon_type
		print("Ingrese un tipo de Pokémon válido.")


# Filter Pokemon whose type matches the requested type.
def find_by_type(pokemons, pokemon_type):
	"""Return Pokemon with a case-insensitive matching type."""
	requested_type = pokemon_type.casefold()
	return [
		pokemon
		for pokemon in pokemons
		# Use str.casefold() for case-insensitive comparison.
		if str(pokemon.get("type", "")).casefold() == requested_type 
	]


# Display the names of all matching Pokemon.
def display_pokemons(pokemons):
	"""Print the names of the matching Pokemon."""
	if not pokemons:
		print("No existen Pokémon de ese tipo.")
		return

    
	print("Los Pokémon que existen de ese tipo son:")
	for pokemon in pokemons:
		print(pokemon.get("name", "Nombre no disponible"))
		print()  # Print a blank line between each Pokemon.


# Main function to load the Pokemon, search by type, and display the results.
def main():
    """Load the Pokemon, search by type, and display the results."""

    # Locate the JSON file created in the previous exercise.
    filename = Path(__file__).resolve().parent / "pokemons.json"

    try:
        pokemons = read_pokemons(filename)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {filename}")
        return
    except (OSError, UnicodeError, ValueError) as error:
        print(f"No se pudo leer el archivo de Pokémon: {error}")
        return

    pokemon_type = ask_pokemon_type()
    matching_pokemons = find_by_type(pokemons, pokemon_type)
    display_pokemons(matching_pokemons)


# Run the program only when this file is executed directly.
if __name__ == "__main__":
	main()
