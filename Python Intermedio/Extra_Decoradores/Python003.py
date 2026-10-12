"""
Student: Cesar Lanuza Urbina
Program: @log_call and @validate_numbers decorators using functools.wraps to preserve function metadata and enforce argument validation.
"""

from datetime import datetime
from functools import wraps
from numbers import Number


# Log the function's name, arguments, call time, and return value.
def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Capture the local date and time when the function is called.
        call_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        result = function(*args, **kwargs)

        # Include both positional and keyword arguments in the log.
        arguments = [repr(value) for value in args]
        arguments.extend(f"{key}={value!r}" for key, value in kwargs.items())
        print(
            f"func:{function.__name__} - args: {', '.join(arguments)} - "
            f"[{call_time}] - Resultado: {result}"
        )
        return result

    return wrapper


# Validate every argument before executing the decorated function.
def validate_numbers(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Reject nonnumeric values and booleans, which Python treats as integers.
        for value in (*args, *kwargs.values()):
            if not isinstance(value, Number) or isinstance(value, bool):
                raise TypeError("Todos los argumentos deben ser numéricos")

        return function(*args, **kwargs)

    return wrapper


@log_call
@validate_numbers
def multiply(first_number, second_number):
    # Return the product of the two validated numbers.
    return first_number * second_number


# Run the example only when this file is executed directly.
if __name__ == "__main__":
    result = multiply(8, 15)
    print(f"Resultado {result}")
