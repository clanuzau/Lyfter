"""
Student : Cesar Lanuza Urbina
Program : Demonstrate multiple inheritance by creating a car.
"""


class Engine:
    # Initialize the engine attributes used by the car.
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.engine_running = False

    # Start the engine before driving.
    def start_engine(self):
        self.engine_running = True
        print("Motor encendido.")

    # Stop the engine when the trip is over.
    def stop_engine(self):
        self.engine_running = False
        print("Motor apagado.")


class Radio:
    # Initialize the radio independently from the engine.
    def __init__(self, station):
        self.station = station

    # Play the selected radio station.
    def play_radio(self):
        print(f"Reproduciendo la estacion {self.station}.")


# Car inherits attributes and methods from two parent classes.
class Car(Engine, Radio):
    # Initialize both parents explicitly because they have separate constructors.
    def __init__(self, brand, model, horsepower, station):
        Engine.__init__(self, horsepower)
        Radio.__init__(self, station)
        self.brand = brand
        self.model = model

    # Display the car information, including an inherited attribute.
    def show_information(self):
        print(f"Automovil: {self.brand} {self.model}")
        print(f"Potencia: {self.horsepower} HP")

    # Check the inherited engine state before allowing the car to move.
    def drive(self):
        if self.engine_running:
            print(f"El {self.brand} {self.model} esta en movimiento.")
        else:
            print("Primero debes encender el motor.")


def main():
    # Create one object that combines the behavior of Engine and Radio.
    car = Car("Toyota", "Corolla", 140, "101.5 FM")
    car.show_information()

    # Demonstrate the engine check and methods inherited from both parents.
    car.drive()
    car.start_engine()
    car.play_radio()
    car.drive()
    car.stop_engine()


# Run the demonstration only when this file is executed directly.
if __name__ == "__main__":
    main()
