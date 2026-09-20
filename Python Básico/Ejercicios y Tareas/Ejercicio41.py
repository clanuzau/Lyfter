"""
Student: Cesar Lanuza Urbina
Program: Count video games by genre and display the results alphabetically.
"""

import csv
from pathlib import Path


# Locate the CSV next to this script, regardless of the working directory.
FILE_PATH = Path(__file__).resolve().parent / "videogames.csv"

# The CSV file is expected to have four columns: name, genre, developer, and ESRB rating.
def read_games(filename=FILE_PATH):
    """Read the CSV file and return its valid video game records."""
    games = []

    # Open the CSV file with UTF-8 encoding and handle potential errors.
    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        # Skip the header because it contains column names.
        next(reader, None)

        for record in reader:
            # Ignore empty rows and reject records with missing or extra fields.
            if not record:
                continue
            if len(record) != 4:
                print(f"Registro inválido en la línea {reader.line_num}: se esperan 4 campos.")
                continue

            games.append(record)

    return games

# Function to count how many video games belong to each genre.
def count_genres(games):
    """Count how many video games belong to each genre."""
    genre_counts = {}

    for game in games:
        # A quoted CSV field may contain several comma-separated genres.
        genres = game[1].split(",")
        counted_genres = set() # Track which genres have already been counted for this game.

        for genre in genres:
            genre = genre.strip()

            # Skip empty names and count each genre only once per game.
            if not genre or genre in counted_genres:
                continue

            # Increment the count for this genre, initializing it to zero if necessary.    
            genre_counts[genre] = genre_counts.get(genre, 0) + 1 
            counted_genres.add(genre)

    return genre_counts


def display_genres(genre_counts, total_games):
    """Display an alphabetical genre summary and overall totals."""
    # Explain when the file contains no genres to display.
    if not genre_counts:
        print("No se encontraron géneros en el archivo.")
    else:
        print()
        print("Géneros encontrados:")
        print()

        # Display each genre and its count on a separate line.
        for genre in sorted(genre_counts, key=str.casefold):
            print(f"{genre}: {genre_counts[genre]}")

    # Report distinct genres and the number of records read from the CSV.
    print(f"\nTotal de géneros distintos: {len(genre_counts)}")
    

    print(f"Total de videojuegos: {total_games}")

    # A game with multiple genres contributes once to each genre's count.
    print(f"Suma de los conteos por género: {sum(genre_counts.values())}")
    print()
    


def main():
    """Coordinate reading the CSV, counting genres, and showing results."""
    # Report file errors with a readable message.
    try:
        games = read_games()
    except FileNotFoundError:
        print(f"No se encontró el archivo: {FILE_PATH}")
        return
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"No se pudo leer el archivo CSV: {error}")
        return

    genre_counts = count_genres(games)
    display_genres(genre_counts, len(games))


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
