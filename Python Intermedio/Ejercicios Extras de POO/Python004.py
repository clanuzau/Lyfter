"""
Student: Cesar Lanuza Urbina
Program: Python Intermedio - Calculate the area and perimeter of a rectangle given its width and height
"""

class Rectangle:
    """Represent a rectangle with non-negative dimensions."""

    def __init__(self, width, height):
        # Reject negative dimensions before storing the rectangle's attributes.
        if width < 0 or height < 0:
            raise ValueError("El ancho y la altura no pueden ser negativos.")

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


# main program to demonstrate the Rectangle class.
if __name__ == "__main__":
    # Read the dimensions and allow decimal values.
    height = float(input("Ingrese la altura: "))
    width = float(input("Ingrese el ancho: "))

    # Create a validated rectangle and display results without trailing zeros.
    rectangle = Rectangle(width, height)
    print(f"El área del rectángulo es: {rectangle.get_area():g}")
    print(f"El área del perímetro es: {rectangle.get_perimeter():g}")
