"""
Student: Cesar Lanuza Urbina
Program: Python Intermedio - Class Animal to demonstrate inheritance and method overriding.
"""

class Animal:
    """Represent an animal with a name and a generic sound."""

    # Initialize the animal with a name.
    def __init__(self, name):
        """Store the animal's name."""
        self.name = name

    # Define a method to return the default sound for an animal.
    def speak(self):
        """Return the default sound for an animal."""
        return "Hacen un sonido"


# Create a Dog class that inherits from Animal and overrides the speak method.
class Dog(Animal):
    """Inherit the animal's name and provide a dog-specific sound."""

    # Override the speak method to return a dog's bark.
    def speak(self):
        """Override the base method to return a dog's bark."""
        return "Guau"


# Create a Cat class that inherits from Animal and overrides the speak method.
class Cat(Animal):
    """Inherit the animal's name and provide a cat-specific sound."""

    # Override the speak method to return a cat's meow.
    def speak(self):
        """Override the base method to return a cat's meow."""
        return "Miau"


if __name__ == "__main__":
    # Create a dog and a cat using the constructor inherited from Animal.
    dog = Dog("Firulais") # Create a Dog instance with the name "Firulais"
    cat = Cat("Michi")  # Create a Cat instance with the name "Michi"

    # Create a base-class instance to use the default animal sound.
    base = Animal("Animal")  

    # Display the overridden sounds and the default base-class sound.
    print()
    print(f"El perro hace: {dog.speak()}")  # Guau
    print(f"El gato hace: {cat.speak()}")  # Miau
    print(f"Otros {base.speak()}")  # Hace un sonido
    print()
