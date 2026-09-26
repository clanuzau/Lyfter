"""
Student: Cesar Lanuza Urbina
Program: Python Intermedio - Calculate the area of a circle given its radius
"""
from math import isfinite, pi


class Circle:
    # Initialize the circle with a given radius.
    def __init__(self, radius):
        # Store the circle's radius.
        self.radius = radius 

    # Method to calculate the area of the circle.
    def get_area(self):
        # Calculate the area using the formula: pi * radius squared.
        return pi * self.radius ** 2


if __name__ == "__main__":
    # Keep asking until the user enters a finite, nonnegative radius.
    while True:
        try:
            # Accept either a decimal point or a decimal comma.
            radius = float(input("Ingrese la medida del radio del circulo: ").strip().replace(",", "."))
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")
            continue

        if not isfinite(radius) or radius < 0:
            print("El radio debe ser un número finito mayor o igual a cero.")
            continue

        break

    # Create the circle with the radius supplied by the user.
    circle = Circle(radius) 
    print(f"Radio del círculo es: {circle.radius:.2f}")
    print(f"Área del círculo: {circle.get_area():.2f}")
