"""
Student: Cesar Lanuza Urbina
Program: Start the student management console application.
"""

from menu import run_menu


def main():
    """Create the session's student list and start the menu."""
    students = []
    try:
        run_menu(students)
    except (EOFError, KeyboardInterrupt):
        # End console input cleanly without writing or changing any CSV file.
        print("\nSesión finalizada. Solo se conservan los datos exportados previamente.")


if __name__ == "__main__":
    main()
