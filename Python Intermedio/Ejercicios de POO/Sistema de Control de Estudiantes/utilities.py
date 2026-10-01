"""
Student: Cesar Lanuza Urbina
Program: Import and export student records using CSV files.
"""

import csv
from pathlib import Path

import actions
import data


# Import student records from a CSV file, validating each record before adding it to the list.
def import_students(file_path=data.FILE_PATH):
    """Return a new list only after every record has passed validation."""
    # The CSV file is opened in text mode with UTF-8 encoding to support accented names.
    students = []
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, strict=True)
        data.validate_csv_headers(reader.fieldnames)
        for row in reader:
            # Convert each validated CSV dictionary into a student object.
            student = data.parse_student_row(row, reader.line_num)
            if actions.student_exists(students, student.full_name, student.section):
                raise ValueError(f"Fila {reader.line_num}: el nombre y la sección están duplicados.")
            students.append(student)
    return students


# Write the current student records to the selected CSV file.
def export_students(students, file_path=data.FILE_PATH):
    """Write the current records, preserving existing files when there is no data."""
    if not students:
        raise ValueError("No hay estudiantes para exportar.")
    file_path = Path(file_path) # Convert the file path to a Path object for easier manipulation.
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data.FIELDNAMES)
        writer.writeheader() #  Write the header row to the CSV file.
        # Convert objects back to dictionaries only when writing CSV rows.
        writer.writerows(student.to_dict() for student in students)
