"""
Student: Cesar Lanuza Urbina
Program: Register, validate, display, and analyze students in memory.
"""

import re


SUBJECTS = {
    "spanish": "Español",
    "english": "Inglés",
    "social_studies": "Estudios Sociales",
    "science": "Ciencias",
}

# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def normalize_name(full_name):
    """Remove surrounding and repeated whitespace without changing case."""
    return " ".join(full_name.split())


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def is_valid_name(full_name):
    """Accept names containing letters, spaces, apostrophes, or hyphens."""
    if not isinstance(full_name, str):
        return False
    full_name = normalize_name(full_name)
    return any(character.isalpha() for character in full_name) and all(
        character.isalpha() or character in " '-’" for character in full_name
    )


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def is_valid_section(section):
    """Accept a number from 1 to 99 followed by one ASCII letter."""
    return isinstance(section, str) and re.fullmatch(
        r"[1-9][0-9]?[A-Z]", section.strip().upper()
    ) is not None


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.    
def is_valid_grade(value):
    """Accept numeric grades between zero and one hundred, inclusive."""
    # Booleans are numbers in Python but are not valid student grades.
    # The range comparison also rejects NaN and infinity.
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and 0 <= value <= 100
    )


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def ask_confirmation(message):
    """Repeat the question until the user enters yes or no."""
    while True:
        answer = input(f"{message} (s/n): ").strip().casefold()
        if answer in ("s", "si", "sí", "y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Ingrese s para confirmar o n para cancelar.")
        print()


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def read_name():
    """Read a nonempty name using the same rules as CSV imports."""
    while True:
        full_name = normalize_name(input("Nombre completo: "))
        if is_valid_name(full_name):
            return full_name
        print("Use letras, espacios, apóstrofos o guiones para el nombre.")


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def read_section():
    """Read and normalize a section such as 1A or 11B."""
    while True:
        section = input("Sección (por ejemplo, 11B): ").strip().upper()
        if is_valid_section(section):
            return section
        print("Use un número del 1 al 99 seguido de una letra, por ejemplo, 11B.")


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def read_grade(subject_name):
    """Keep asking until the user enters a grade within the allowed range."""
    while True:
        try:
            grade = float(input(f"Nota de {subject_name} (0-100): "))
        except ValueError:
            print("Ingrese un número. Use punto para los decimales, por ejemplo, 85.5.")
            continue
        if is_valid_grade(grade):
            return grade
        print("La nota debe estar entre 0 y 100.")


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def read_student():
    """Build a complete student record before adding it to the active list."""
    student = {"full_name": read_name(), "section": read_section()}
    for subject, label in SUBJECTS.items():
        student[subject] = read_grade(label)
    return student


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def find_student(students, full_name, section):
    """Return a matching student, ignoring name spacing and letter case."""
    normalized_name = normalize_name(full_name).casefold()
    normalized_section = section.strip().upper() # Normalize section for comparison
    for student in students:
        if (
            normalize_name(student["full_name"]).casefold() == normalized_name
            and student["section"].strip().upper() == normalized_section
        ):
            return student
    return None


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def student_exists(students, full_name, section):
    """Check whether the same name and section are already registered."""
    return find_student(students, full_name, section) is not None


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def add_students(students):
    """Register students one at a time without imposing a fixed limit."""
    while True:
        student = read_student()
        if student_exists(students, student["full_name"], student["section"]): #    Check for duplicates
            print("Ya existe un estudiante con este nombre y sección.")
        else:
            students.append(student)
            print()
            print("Estudiante registrado correctamente.")
        if not ask_confirmation("¿Desea agregar otro estudiante?"):
            return


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def calculate_student_average(student):
    """Calculate an average from the original four grades without rounding."""
    return sum(student[subject] for subject in SUBJECTS) / len(SUBJECTS)


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def display_students(students):
    """Display each student's identity, four grades, and average."""
    if not students:
        print("No hay estudiantes registrados.")
        return
    # Display students in the order they were registered, starting at 1.
    for position, student in enumerate(students, start=1):
        print(f"\n{position}. {student['full_name']} | Sección: {student['section']}")

        for subject, label in SUBJECTS.items():
            print(f"   {label}: {student[subject]:.2f}")
        print(f"   Promedio: {calculate_student_average(student):.2f}")
        print()


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def get_top_students(students, limit=3):
    """Sort by descending average, then name and section for tied averages."""
    # sorted() creates a new list and preserves the original registration order.
    ranked_students = sorted(
        students,
        key=lambda student: (
            -calculate_student_average(student),
            normalize_name(student["full_name"]).casefold(),
            student["section"],
        ),
    )
    return ranked_students[:max(0, limit)]


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def display_top_students(students):
    """Display up to three students with the highest averages."""
    print("\nLos 3 mejores estudiantes")
    display_students(get_top_students(students))


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def calculate_overall_average(students):
    """Return the mean of individual averages, or None for an empty list."""
    if not students:
        return None
    return sum(calculate_student_average(student) for student in students) / len(students)


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def display_overall_average(students):
    """Display the overall average rounded only for presentation."""
    average = calculate_overall_average(students)
    if average is None:
        print("No hay estudiantes registrados.")
    else:
        print(f"Promedio general: {average:.2f}")


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def delete_student(students):
    """Remove only the identified student after explicit confirmation."""
    if not students:
        print("No hay estudiantes registrados.")
        return
    student = find_student(students, read_name(), read_section())
    if student is None:
        print("No se encontró al estudiante.")
        return
    display_students([student]) # Display the student to be deleted for confirmation
    if ask_confirmation("¿Desea eliminar a este estudiante de la sesión actual?"):
        students.remove(student)
        print("Estudiante eliminado. Exporte los datos para guardar este cambio.")
        print()
    else:
        print("Eliminación cancelada.")
        print()


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def get_failed_subjects(student):
    """Return the labels of subjects with a grade strictly below sixty."""
    return [label for subject, label in SUBJECTS.items() if student[subject] < 60]


# The following functions are used by menu.py and actions.py to validate input, read student data, and perform calculations.
def display_failing_students(students):
    """Display students with at least one failing grade and those subjects."""
    if not students:
        print("No hay estudiantes registrados.")
        return
    found = False
    for student in students:
        failed_subjects = get_failed_subjects(student)
        if failed_subjects:
            found = True
            print(f"{student['full_name']} | Sección: {student['section']}")
            print(f"Materias reprobadas: {', '.join(failed_subjects)}")
    if not found:
        print("No hay estudiantes reprobados.")
        print()
