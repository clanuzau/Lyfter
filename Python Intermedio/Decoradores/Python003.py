"""
Student: Cesar Lanuza Urbina
Program: This module demonstrates the use of decorators in Python to enforce age restrictions on user actions.
It defines a User class with a date of birth and calculates the user's age.
The require_adult decorator checks if a user is at least 18 years old before allowing access to certain functions.
"""

from datetime import date
from functools import wraps


# Define the User class to represent a user with a date of birth and a calculated age.
class User:
    """Represent a user with a date of birth and a calculated age."""

    # Initialize the User class with a date of birth and validate the input.
    def __init__(self, date_of_birth):
        """Initialize the user with a valid date of birth."""
        if not isinstance(date_of_birth, date):
            raise TypeError("fecha de nacimiento debe ser un objeto de tipo date.")
        if date_of_birth > date.today():
            raise ValueError("fecha de nacimiento no puede ser una fecha futura.")

        self.date_of_birth = date_of_birth # Store the user's date of birth.

    @property
    def age(self):
        """Return the user's age in completed years."""
        today = date.today()
        years = today.year - self.date_of_birth.year

        # Subtract one year if this year's birthday has not occurred yet.
        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            years -= 1

        return years

# Decorator to enforce that a user is an adult (18 years or older).
def require_adult(function):
    """Require the first parameter, named user, to be a User aged 18 or older."""

    @wraps(function)  # Preserve the original function's name and documentation.
    def wrapper(user, *args, **kwargs):
        """Validate the user before executing the decorated function."""
        if not isinstance(user, User):
            raise TypeError("El argumento de usuario debe ser una instancia User.")

        # Reject minors before the decorated function can perform any action.
        if user.age < 18:
            raise ValueError("El usuario debe ser mayor de edad (18 años o más) para acceder a esta función.")

        return function(user, *args, **kwargs)

    return wrapper # Return the wrapper function to replace the original function.


# Example usage of the require_adult decorator.
@require_adult
def access_restricted_content(user):
    """Return an access message after the adult check succeeds."""
    print()
    return f"Acceso concedido a contenido restringido para el usuario de {user.age} años."


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    adult_user = User(date(1990, 1, 1))
    print(access_restricted_content(adult_user))

    # A user born today is always a minor, keeping the example valid over time.
    minor_user = User(date.today())
    try:
        access_restricted_content(user=minor_user) # Attempt to access restricted content with a minor user.
    except ValueError as error:
        print(f"Error: {error}")
