"""
Student: Cesar Lanuza Urbina
Program: Python Intermedio - Calculate the area and perimeter of a rectangle given its width and height
"""

class Rectangle:
    """Represent a rectangle with non-negative dimensions."""

    def __init__(self, width, height):
        """Validate and store the rectangle dimensions."""
        # Reject negative dimensions before storing the rectangle's attributes.
        if width < 0 or height < 0:
            raise ValueError("Existe un valor negativo, los valores deben ser positivos")

        self.width = width
        self.height = height

    # Method to calculate the area of the rectangle.
    def get_area(self):
        """Return the area by multiplying width and height."""
        return self.width * self.height

    # Method to calculate the perimeter of the rectangle.
    def get_perimeter(self):
        """Return the total length of the rectangle's four sides."""
        return 2 * (self.width + self.height)


def read_dimension(prompt):
    """Read a numeric dimension, allowing negative values at this stage."""
    # Convert user input and provide a clear message for non-numeric values.
    try:
        value = float(input(prompt))
    except ValueError:
        raise ValueError("Debe ingresar un valor numérico válido.") from None

    return value


if __name__ == "__main__":
    # Capture invalid input and display the error without a traceback.
    try:
        # Collect both dimensions before checking for negative values.
        height = read_dimension("Ingrese la altura: ")
        width = read_dimension("Ingrese el ancho: ")
        # Validate both values together when creating the rectangle.
        rectangle = Rectangle(width, height)
    except ValueError as error:
        print(error)
    else:
        # Display the results only when both dimensions are valid.
        print()
        print(f"El área del rectángulo es: {rectangle.get_area():g}")
        print(f"El perímetro del rectángulo es: {rectangle.get_perimeter():g}")
        print()
