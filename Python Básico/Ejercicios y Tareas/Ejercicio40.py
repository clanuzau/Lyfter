"""
Student: Cesar Lanuza Urbina
Program: Read video games from a CSV file and filter them by ESRB rating.
"""

import csv
from pathlib import Path


# Locate the CSV in the same folder as this script.
FILE_PATH = Path(__file__).resolve().parent / "videogames.csv"


def read_games(filename=FILE_PATH):
    """Read and return the video game records from the CSV file."""
    games = []

    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        # Skip the header row, which contains the column names.
        next(reader, None)

        for record in reader:
            # Skip empty rows and records that do not have four fields.
            if not record:
                continue
            if len(record) != 4:
                print(f"Registro inválido en la línea {reader.line_num}: se esperan 4 campos.")
                continue

            games.append(record)

    return games


def normalize_rating(rating):
    """Extract an uppercase ESRB code from values such as 'T (Teen)'."""
    # Remove the optional description so both CSV rating formats match.
    return rating.split("(", 1)[0].strip().upper()


def ask_rating():
    """Ask the user for a nonempty ESRB rating."""
    while True:
        rating = normalize_rating(input("Ingrese una clasificación ESRB (por ejemplo, T): "))

        # Require a rating before searching the records.
        if rating:
            return rating
        print("Debe ingresar una clasificación ESRB.")


def filter_games(games, rating):
    """Return all video games whose ESRB code matches the requested rating."""
    matches = []
    for game in games:
        # Compare exact codes to keep E and E10+ as separate ratings.
        if normalize_rating(game[3]) == normalize_rating(rating):
            matches.append(game)
    return matches


def display_games(games):
    """Display each matching video game with readable labels."""
    for name, genre, developer, rating in games:
        print(f"Nombre: {name}")
        print(f"Género: {genre}")
        print(f"Desarrollador: {developer}")
        print(f"Clasificación: {rating}")
        print()


def main():
    """Coordinate file reading, user input, filtering, and output."""
    # Report file reading errors before asking the user for a rating.
    try:
        games = read_games()
    except FileNotFoundError:
        print(f"No se encontró el archivo: {FILE_PATH}")
        return
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"No se pudo leer el archivo CSV: {error}")
        return

    rating = ask_rating()
    matches = filter_games(games, rating)

    # Show the matching games or explain that the search returned no results.
    if matches:
        print(f"\nVideojuegos con clasificación ESRB {rating}:\n")
        display_games(matches)
    else:
        print(f"No se encontraron videojuegos con la clasificación ESRB {rating}.")


# Start the program only when this script is executed directly.
if __name__ == "__main__":
    main()
