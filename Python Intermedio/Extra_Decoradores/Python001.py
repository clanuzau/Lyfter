""" 
Student: Cesar Lanuza Urbina
Program: Python Intermedio - Decoradores @repeat_twice ejemplo de uso
"""
from functools import wraps


# Run the decorated function twice with the same arguments.
def repeat_twice(function):
    # Preserve the original function's name and documentation.
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Forward positional and keyword arguments to both calls.
        function(*args, **kwargs)
        return function(*args, **kwargs)

    return wrapper


@repeat_twice
def greet(name):
    # Print a greeting using the provided name.
    print(f"Hola, {name}")
   


# Run the example only when this file is executed directly.
if __name__ == "__main__":
    greet("Cesar")
