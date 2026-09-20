"""
Program: Phyton038.py - Alternate version of Phyton037 that stores the video game
information in a TAB-separated file (video_games.csv) instead of a comma-separated file.
Student: Cesar Lanuza Urbina
"""

import csv
import os

# File where the video game records will be saved (next to this script).
FILENAME = "video_games.c02.sv"

# Full path to the file, built from the location of this program.
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILENAME)

# Column names for the tab-separated file.
# These names will be used as keys in the dictionaries that represent each video game.
FIELDS = ["nombre", "genero", "desarrollador", "clasificacion"]

# Separator used between the columns: a TAB character instead of a comma.
DELIMITER = "\t"


# Function that asks the user for the information of a single video game
# and returns it as a dictionary.
def input_records():
    """Function that asks the user for the information of a single video game."""
    name = input("Nombre: ").strip()
    genre = input("Genero: ").strip()
    developer = input("Desarrollador: ").strip()
    esrb_rating = input("Clasificacion ESRB: ").strip()

    # Build a dictionary with the video game data.
    record = {
        "nombre": name,
        "genero": genre,
        "desarrollador": developer,
        "clasificacion": esrb_rating,
    }
    return record


# Function that asks the user if they want to continue adding records.
# Returns True if the answer is S (or yes), and False otherwise.
def wants_to_continue():
    """Function that asks the user if they want to continue adding records."""
    answer = input("Desea continuar? [S/N]: ").strip().upper()
    return answer in ("S", "SI", "SÍ", "YES")


# Function that collects all the records entered by the user into a list
# of dictionaries and returns that list.
def save_records():
    """Function that collects all the video game records entered by the user."""
    records = []  # Initialize an empty list to store the records.

    print()
    print("=== INGRESO DE VIDEOJUEGOS ===")
    while True:
        print()
        record = input_records()  # Ask the user for one video game.
        records.append(record)  # Store the record in the list.

        print()
        if not wants_to_continue():  # Ask if the user wants to add more.
            break

    return records


# Function that writes the list of records to the tab-separated file.
# If the file does not exist, it creates it and writes the header row.
# If the file already exists, it appends the new records at the end.
def write_records(records, filename=FILE_PATH):
    """Function that writes the list of video game records to a tab-separated file."""
    # Empty files also need a header; preserve records already on disk.
    file_has_content = os.path.exists(filename) and os.path.getsize(filename) > 0
    needs_newline = False
    if file_has_content:
        with open(filename, "rb") as existing_file:
            existing_file.seek(-1, os.SEEK_END)
            needs_newline = existing_file.read(1) not in (b"\n", b"\r")

    # Open the file in append mode (creates it if it does not exist).
    with open(filename, "a", encoding="utf-8", newline="") as file:
        # Create a writer that uses a TAB as the column separator instead of a comma.
        writer = csv.DictWriter(file, fieldnames=FIELDS, delimiter=DELIMITER)

        # Write the header row when the file is new or empty.
        if needs_newline:
            file.write("\n")
        if not file_has_content:
            writer.writeheader()

        # Write each record as a new row in the file.
        for record in records:
            writer.writerow(record)

    print()
    print(f"Se guardaron {len(records)} registro(s) en el archivo '{filename}'.")


# Main function that coordinates the record input and file writing process.
def main():
    print()
    print("=== VIDEOJUEGOS - ARCHIVO video_games.csv (separado por tabulacion) ===")

    # Ask the user for all the records first.
    records = save_records()

    # If at least one record was entered, save it to the file.
    if records:
        try:
            write_records(records)
        except (OSError, UnicodeError, csv.Error) as error:
            print(f"No se pudo guardar el archivo: {error}")
            return
    else:
        print()
        print("No se ingresaron registros. No se creo el archivo.")

    print()
    print("Programa finalizado.")
    print()


if __name__ == "__main__":
    main()
