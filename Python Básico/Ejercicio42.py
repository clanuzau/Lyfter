"""
Student: Cesar Lanuza Urbina
Program: Read video games from a CSV file and search by developer.
"""

import csv
from pathlib import Path


# Locate the CSV next to this script, regardless of the working directory.
FILE_PATH = Path(__file__).resolve().parent / "videogames.csv"


def read_games(filename=FILE_PATH):
    """Read the CSV file and return its valid video game records."""
    games = []

    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        # Skip the header because it contains column names.
        next(reader, None)

        for record in reader:
            # Ignore empty rows and reject records without exactly four fields.
            if not record:
                continue
            if len(record) != 4:
                print(f"Registro inválido en la línea {reader.line_num}: se esperan 4 campos.")
                continue

            games.append(record)

    return games


def ask_developer():
    """Ask the user for a developer name."""
    while True:
        developer = input("Ingrese el nombre de un desarrollador (ej. Ubisoft): ").strip()

        # Require a name so an empty search does not match every developer.
        if developer:
            return developer
        print("Debe ingresar el nombre de un desarrollador.")


def filter_games(games, developer):
    """Find games whose developer contains the requested name."""
    matches = []
    search_name = developer.strip().casefold()

    for game in games:
        # Match partial names without case sensitivity, such as Ubisoft Montreal.
        if search_name in game[2].strip().casefold():
            matches.append(game)

    return matches


def display_games(games, developer):
    """Display the matching games as a readable list."""
    # Explain when no developer matches the user's search.
    if not games:
        print(f"\nNo se encontraron videojuegos desarrollados por {developer}.")
        return

    print(f"\nVideojuegos desarrollados por {developer}:\n")

    # Show each game's name, rating, and genre on its own line.
    for name, genre, studio, rating in games:
        print(f"- {name} (Clasificación: {rating}, Género: {genre})")


def main():
    """Coordinate file reading, developer input, filtering, and output."""
    # Report file reading errors before asking for a developer.
    try:
        games = read_games()
    except FileNotFoundError:
        print(f"No se encontró el archivo: {FILE_PATH}")
        return
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"No se pudo leer el archivo CSV: {error}")
        return

    developer = ask_developer()
    matches = filter_games(games, developer)
    display_games(matches, developer)


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
