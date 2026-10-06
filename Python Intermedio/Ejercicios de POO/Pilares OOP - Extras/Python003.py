"""
Student: Cesar Lanuza Urbina
Program : This code defines a base class `Vehicle` and two subclasses `Car` and `Motorcycle`, 
demonstrating the principles of object-oriented programming (OOP) in Python. 
The base class contains common attributes and methods, while the subclasses extend the functionality 
to include specific details relevant to their types. The `main` function creates instances of these classes and validates 
their behavior through assertions and print
"""

class Vehicle:
    def __init__(self, brand, year):
        # Store the common attributes using the protected naming convention.
        self._brand = brand
        self._year = year

    # Define a method to return a description of the vehicle, which can be overridden by subclasses.
    def get_info(self):
        # Return the description shared by all vehicles.
        return f"{self._brand} ({self._year})"


# Subclasses that extend Vehicle must implement their own get_info method to provide additional details specific to their type.
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        # Initialize the inherited attributes and store the number of doors.
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self):
        # Extend the base description with the number of doors.
        return f"{super().get_info()} - {self.doors} puertas"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        # Initialize the inherited attributes and store the motorcycle type.
        super().__init__(brand, year)
        self.type = type

    def get_info(self):
        # Extend the base description with the motorcycle type.
        return f"{super().get_info()} - Tipo: {self.type}"


def main():
    # Create the example vehicles and validate their descriptions.
    vehicle1 = Car("Toyota", 2020, 4)
    vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

    # Validate that the get_info method returns the expected descriptions for each vehicle type.
    assert Vehicle("Honda", 2021).get_info() == "Honda (2021)"
    assert vehicle1.get_info() == "Toyota (2020) - 4 puertas"
    assert vehicle2.get_info() == "Yamaha (2022) - Tipo: Deportiva"

    # Display each vehicle's description using its overridden method.
    print()
    print(vehicle1.get_info())
    print(vehicle2.get_info())
    print()


if __name__ == "__main__":
    main()
