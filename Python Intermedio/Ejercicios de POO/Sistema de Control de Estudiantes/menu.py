"""
Student: Cesar Lanuza Urbina
Program: Display the console menu and coordinate student operations.
"""

import csv
from pathlib import Path

import actions
import data
import utilities


def display_menu():
    """Show all available actions and the explicit persistence options."""
    print("\nSistema de Control de Estudiantes")
    print("1. Registrar estudiantes")
    print("2. Mostrar todos los estudiantes")
    print("3. Mostrar los 3 mejores estudiantes")
    print("4. Mostrar el promedio general")
    print("5. Exportar estudiantes a CSV")
    print("6. Importar estudiantes desde CSV")
    print("7. Eliminar un estudiante")
    print("8. Mostrar estudiantes reprobados")
    print("0. Salir")


def get_menu_option():
    """Read a valid option without converting arbitrary input to an integer."""
    while True:
        option = input("Seleccione una opción: ").strip()
        if option in ("0", "1", "2", "3", "4", "5", "6", "7", "8"):
            return option
        print("Opción inválida. Ingrese un número del 0 al 8.")


def export_current_students(students, file_path=data.FILE_PATH):
    """Confirm overwrites and report success only after the file is written."""
    if not students:
        print("No hay estudiantes para exportar. Los archivos existentes no se han modificado.")
        return
    file_path = Path(file_path)
    if file_path.is_file() and not actions.ask_confirmation(
        f"¿Desea sobrescribir el archivo CSV existente en {file_path}?"
    ):
        print("Exportación cancelada.")
        return
    utilities.export_students(students, file_path)
    print(f"Se exportaron {len(students)} estudiante(s) a {file_path}.")


def import_current_students(students, file_path=data.FILE_PATH):
    """Validate the whole file before confirming replacement of session data."""
    imported_students = utilities.import_students(file_path)
    if students and not actions.ask_confirmation(
        f"¿Desea reemplazar los {len(students)} estudiante(s) actuales por "
        f"{len(imported_students)} estudiante(s) importados?"
    ):
        print("Importación cancelada.")
        return
    # Update the shared list only after validation and confirmation succeed.
    students[:] = imported_students
    print(f"Se importaron {len(students)} estudiante(s) desde {file_path}.")


def run_menu(students, file_path=data.FILE_PATH):
    """Keep the session running and handle expected file errors explicitly."""
    print("Los datos permanecen en memoria hasta que seleccione Exportar estudiantes a CSV.")
    print(f"Archivo CSV: {file_path}")
    while True:
        # Show the menu and get a valid option from the user.
        display_menu()
        # Read the option and call the corresponding action, handling exceptions.
        option = get_menu_option()
        try:
            if option == "1":
                actions.add_students(students)
            elif option == "2":
                actions.display_students(students)
            elif option == "3":
                actions.display_top_students(students)
            elif option == "4":
                actions.display_overall_average(students)
            elif option == "5":
                export_current_students(students, file_path)
            elif option == "6":
                import_current_students(students, file_path)
            elif option == "7":
                actions.delete_student(students)
            elif option == "8":
                actions.display_failing_students(students)
            else:
                print("Hasta luego. Solo se conservan los datos exportados previamente.")
                return
        except FileNotFoundError:
            print(f"No se encontró el archivo CSV: {file_path}. Exporte los estudiantes primero.")
        except PermissionError:
            print("Permiso denegado. Revise el acceso al archivo y si está abierto en otro programa.")
        except UnicodeError:
            print("El archivo CSV debe utilizar la codificación UTF-8.")
        except csv.Error:
            print("No se pudo procesar el archivo CSV. Revise su formato y las comillas de los campos.")
        except ValueError as error:
            print(f"Datos inválidos: {error}")
        except OSError:
            print("No se pudo acceder al archivo CSV. Revise la ruta y el espacio disponible.")
