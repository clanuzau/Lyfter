"""
Task: Phyton Basico - Read and Write Files
Student: Cesar Lanuza Urbina
"""

# This script reads a list of song names from a text file, sorts them alphabetically
# (case-insensitive), and writes the sorted list to a new text file. It uses the os
# module to handle file paths and discards empty lines during the reading process.

import os

# read_songs function reads song names from a specified input file, discarding any empty lines.
def read_songs(input_file):
    """Read the song names from a file and discard empty lines."""
    with open(input_file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

# sort_songs function sorts the list of song names alphabetically without considering letter case.
def sort_songs(songs):
    """Sort the song names alphabetically without considering letter case."""
    return sorted(songs, key=str.casefold)

# write_songs function writes the sorted list of song names to a specified output file.
def write_songs(output_file, songs):
    """Write the sorted song names to a file."""
    with open(output_file, "w", encoding="utf-8") as file:
        for song in songs:
            file.write(f"{song}\n")

# Main function orchestrates the reading, sorting, and writing of song names, handling potential 
# file-related errors.
def Main():
    """Run the song reading, sorting, and writing process in order."""
    current_folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_folder, "Hillsong.txt")
    output_file = os.path.join(current_folder, "Mysongs.txt")

    try:
        songs = read_songs(input_file) # Read the songs from the input file
        sorted_songs = sort_songs(songs) # Sort the songs alphabetically
        write_songs(output_file, sorted_songs) # Write the sorted songs to the output file

        print()
        print(f"Las canciones ordenadas fueron guardadas en: {os.path.basename(output_file)}.")
        print()
    except FileNotFoundError:
        print()
        print(
            f'Error: El archivo de entrada "{os.path.basename(input_file)}" '
            f'no fue encontrado en "{current_folder}".'
        )
        print()
    except PermissionError:
        print()
        print("Error: Permisos denegados mientras leía o escribía en el archivo.")
    except OSError as error:
        print(f"Error mientras se procesaban los archivos: {error}")


if __name__ == "__main__":
    Main()
