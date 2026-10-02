"""
Student: Cesar Lanuza Urbina
Program: Calculate the area and perimeter of circles, squares, and rectangles.
"""

from abc import ABC, abstractmethod
from math import isfinite, pi


# Validate dimensions before using them in geometric calculations.
def validate_dimension(value):
    if not isfinite(value) or value <= 0:
        raise ValueError("La medida debe ser un numero finito mayor que cero.")
    return value


class Shape(ABC):
    # Require every concrete shape to implement its perimeter calculation.
    @abstractmethod
    def calculate_perimeter(self):
        pass

    # Require every concrete shape to implement its area calculation.
    @abstractmethod
    def calculate_area(self):
        pass


# Implement concrete shapes with the required methods and validated dimensions.
class Circle(Shape):
    # Store a valid radius for the circle.
    def __init__(self, radius):
        self.radius = validate_dimension(radius)

    # Calculate the circumference using twice pi times the radius.
    def calculate_perimeter(self):
        return 2 * pi * self.radius

    # Calculate the area using pi times the radius squared.
    def calculate_area(self):
        return pi * self.radius ** 2


class Square(Shape):
    # Store a valid side length for the square.
    def __init__(self, side):
        self.side = validate_dimension(side)

    # Calculate the perimeter by adding the four equal sides.
    def calculate_perimeter(self):
        return 4 * self.side

    # Calculate the area by squaring the side length.
    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    # Store valid width and height dimensions for the rectangle.
    def __init__(self, width, height):
        self.width = validate_dimension(width)
        self.height = validate_dimension(height)

    # Calculate the perimeter by adding both pairs of equal sides.
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    # Calculate the area by multiplying width by height.
    def calculate_area(self):
        return self.width * self.height


# Read a positive, finite dimension and retry invalid entries.
def read_dimension(prompt):
    while True:
        try:
            # Accept decimal values with either a point or a comma.
            value = float(input(prompt).strip().replace(",", "."))
            return validate_dimension(value)
        except (ValueError, OverflowError):
            print("Ingrese un numero valido, finito y mayor que cero.")


# Let the user select a shape and calculate its area and perimeter.
def main():
    while True:
        print("\n1. Circulo")
        print("2. Cuadrado")
        print("3. Rectangulo")
        print("0. Salir")
        option = input("Seleccione una figura: ").strip()

        # Create the selected shape with dimensions validated by the input helper.
        if option == "1":
            shape = Circle(read_dimension("Ingrese el radio: "))
        elif option == "2":
            shape = Square(read_dimension("Ingrese el lado: "))
        elif option == "3":
            width = read_dimension("Ingrese el ancho: ")
            height = read_dimension("Ingrese la altura: ")
            shape = Rectangle(width, height)
        elif option == "0":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opcion invalida. Seleccione 1, 2, 3 o 0.")
            continue

        # Use the common Shape interface to calculate both results.
        try:
            area = shape.calculate_area()
            perimeter = shape.calculate_perimeter()
            if not isfinite(area) or not isfinite(perimeter):
                raise OverflowError
        except OverflowError:
            print("Las medidas son demasiado grandes para calcular el resultado.")
            continue
        print(f"Area: {area:.2f}")
        print(f"Perimetro: {perimeter:.2f}")


# Run the interactive menu only when the file is executed directly.
if __name__ == "__main__":
    main()
