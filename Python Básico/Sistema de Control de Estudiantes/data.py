"""
Student: Cesar Lanuza Urbina
Program: Define the CSV structure and validate student records.
"""

from pathlib import Path

from actions import (
    SUBJECTS,
    is_valid_grade,
    is_valid_name,
    is_valid_section,
    normalize_name,
)

# The CSV file is stored in a subfolder to avoid cluttering the project root.
FIELDNAMES = ["full_name", "section", *SUBJECTS]
# The default file path is relative to this module, so it works even when the
# program is run from a different working directory.
FILE_PATH = Path(__file__).resolve().parent / "storage" / "students.csv"


# Validate the CSV structure and student records before importing.
def validate_csv_headers(fieldnames):
    """Require exactly the expected columns, allowing a different order."""
    if (
        fieldnames is None
        or len(fieldnames) != len(FIELDNAMES)
        or set(fieldnames) != set(FIELDNAMES)
    ):
        raise ValueError(f"Los encabezados del CSV deben contener exactamente: {', '.join(FIELDNAMES)}.")


# Validate the CSV structure and student records before importing.  
def parse_student_row(row, row_number):
    """Validate one complete CSV row and convert its grades to numbers."""
    # DictReader uses a None key for extra fields and None values for missing ones.
    if None in row or any(row.get(field) is None for field in FIELDNAMES):
        raise ValueError(f"Fila {row_number}: se esperan exactamente seis campos.")
    # Validate and normalize the name and section, then validate each grade.
    full_name = normalize_name(row["full_name"])
    section = row["section"].strip().upper()
    if not is_valid_name(full_name):
        raise ValueError(f"Fila {row_number}: el nombre completo no es válido.")
    if not is_valid_section(section):
        raise ValueError(f"Fila {row_number}: la sección no es válida; use un valor como 11B.")
    student = {"full_name": full_name, "section": section}
    # Validate each subject's grade and convert it to a float.
    for subject in SUBJECTS:
        try:
            grade = float(row[subject])
        except ValueError as error:
            raise ValueError(f"Fila {row_number}: la nota de {SUBJECTS[subject]} debe ser numérica.") from error
        if not is_valid_grade(grade):
            raise ValueError(f"Fila {row_number}: la nota de {SUBJECTS[subject]} debe estar entre 0 y 100.")
        student[subject] = grade
    return student
