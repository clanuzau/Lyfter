"""
This example demonstrates how to use a decorator to enforce authentication before allowing access to a function. 
The `requires_login` decorator checks if the user is logged in before executing the decorated function. 
If the user is not authenticated, it raises an exception.
"""   


from functools import wraps


# Track whether the user is currently authenticated.
user_logged_in = False


# Allow the decorated function to run only when the user is logged in.
def requires_login(function):
    # Preserve the original function's name and documentation.
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Check the current login status before each call.
        if user_logged_in is not True:
            raise Exception("Usuario no autenticado")

        # Forward all arguments and return the original function's result.
        return function(*args, **kwargs)

    return wrapper


# Example usage of the `requires_login` decorator.
@requires_login
def view_profile():
    # Display the authenticated user's profile.
    print("Mostrando perfil del usuario")


# Run the example only when this file is executed directly.
if __name__ == "__main__":
    view_profile()
