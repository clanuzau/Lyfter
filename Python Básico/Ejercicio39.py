"""
Student: Cesar Lanuza Urbina
Program: Read video game records from a CSV file and display them on screen.
"""

import csv
from pathlib import Path


# Locate the CSV next to this script, regardless of the working directory.
FILE_PATH = Path(__file__).resolve().parent / "videogames.csv"


def display_game(record):
    """Display the four fields of a video game with readable labels."""
    name, genre, developer, rating = record
    print(f"Nombre: {name}")
    print(f"Género: {genre}")
    print(f"Desarrollador: {developer}")
    print(f"Clasificación: {rating}")
    print()


def read_games(filename=FILE_PATH):
    """Read the CSV row by row and display each valid video game."""
    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file) # Create a CSV reader object to read the file.

        # Skip the header because it contains column names, not a video game.
        next(reader, None)

        for record in reader:
            # Ignore empty rows so they do not appear as incomplete games.
            if not record:
                continue

            # Each video game must contain exactly four fields.
            if len(record) != 4:
                print(f"Registro inválido en la línea {reader.line_num}: se esperan 4 campos.\n")
                continue

            display_game(record)


def main():
    """Coordinate reading the file and handle file access errors."""
    try:
        read_games()
    except FileNotFoundError:
        # Explain the missing file instead of terminating with a traceback.
        print(f"No se encontró el archivo: {FILE_PATH}")
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"No se pudo leer el archivo: {error}")


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
