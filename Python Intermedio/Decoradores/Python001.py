"""
Student: Cesar Lanuza Urbina
Program: Example of a decorator that prints the parameters and return value of a function.
"""


from functools import wraps


def print_arguments_and_return(function):
    """Decorate a function to print its arguments and return value."""

    @wraps(function)  # Preserve the original name and documentation.
    def wrapper(*args, **kwargs):
        """Accept positional and keyword arguments."""
        print()
        print(f"Parámetros de {function.__name__}: {args}, {kwargs}")

        # Call the original function with the received arguments.
        result = function(*args, **kwargs) # Store the result of the original function call.
        print()
        print(f"Retorno de {function.__name__}: {result}")
        print()

        # Return the result to preserve the original behavior.
        return result

    return wrapper # Return the wrapper function to replace the original function.


@print_arguments_and_return
def add(a, b):
    """Return the sum of two numbers."""
    return a + b # Return the sum of the two numbers.


# Run the example only when this file is executed directly.
if __name__ == "__main__":
    add(3, b=5)