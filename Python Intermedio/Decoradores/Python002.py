"""
Student: Cesar Lanuza Urbina
Program: Demonstrate a decorator that validates function arguments.
"""


from functools import wraps
from numbers import Number


# Decorator that validates function arguments.
def require_numeric_arguments(function):
    """Raise TypeError if any supplied argument is not a number."""

    @wraps(function)  # Preserve the original function's name and documentation.
    def wrapper(*args, **kwargs):
        """Validate positional and keyword arguments before calling the function."""
        # Check both argument types; booleans are not accepted as numbers.
        for value in (*args, *kwargs.values()):
            # Validate that the argument is a number and not a boolean.
            if isinstance(value, bool) or not isinstance(value, Number):
                raise TypeError(
                    f"All arguments must be numbers; received {type(value).__name__}."
                )

        # Call the function only after every argument passes validation.
        return function(*args, **kwargs)

    return wrapper


@require_numeric_arguments
# function add() is now decorated with require_numeric_arguments().
def add(first_number, second_number):
    """Return the sum of two numeric arguments."""
    return first_number + second_number


# Run the examples only when this file is executed directly.
if __name__ == "__main__":
    print(add(3, second_number=5))

    # Catch the expected exception so the example ends without a traceback.
    try:
        add(3, "5")
    except TypeError as error:
        print(f"Error: {error}")
