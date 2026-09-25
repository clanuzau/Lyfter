"""
Student: Cesar Lanuza Urbina
Program: Python Intermedio - Create a bus with a maximum capacity and add passengers to it, ensuring that the bus does not exceed its capacity and that each passenger has a valid name.
"""


class Person:
    # Store the person's name so each passenger can be identified.
    def __init__(self, name):
        # Require a nonempty name containing only letters and spaces.
        # isalpha() also accepts accented letters and the letter ñ.
        if not isinstance(name, str):
            raise ValueError("El nombre debe contener solo letras y espacios, sin números.")
        name = name.strip()
        if not name or not all(character.isalpha() or character == " " for character in name):
            raise ValueError("El nombre debe contener solo letras y espacios, sin números.")
        self.name = name


class Bus:
    # Set the capacity and create a separate passenger list 
    # Use isinstance to ensure that the capacity is a nonnegative integer.
    def __init__(self, max_passengers):
        if not isinstance(max_passengers, int) or max_passengers < 0:
            raise ValueError("La capacidad debe ser un entero mayor o igual a cero.")
        self.max_passengers = max_passengers
        self.passengers = [] # Initialize an empty list to hold the passengers.

    # Add one Person instance only when there is an available seat.
    def add_passenger(self, person): 
        if not isinstance(person, Person):
            raise TypeError("El pasajero debe ser una instancia de Person.")

        # Check if the bus is full before adding a new passenger.
        if len(self.passengers) >= self.max_passengers:
            print("El bus está lleno.")
            return False

        # Compare names instead of objects to detect passengers already on board.
        # Ignore capitalization and leading or trailing whitespace.
        passenger_name = person.name.strip().casefold()
        if any(passenger.name.strip().casefold() == passenger_name # Check if the passenger is already on the bus
               for passenger in self.passengers):
            print(f"{person.name.strip()} ya está en el bus.")
            return False

        # Add the person to the bus and return True to indicate success.
        self.passengers.append(person) # Add the person to the bus's passenger list.3
        return True


    # Remove one passenger by name, regardless of their position in the list.
    def remove_passenger(self, name):
        # Validate the name and ignore capitalization and surrounding spaces.
        passenger_name = Person(name).name.casefold()
        for passenger in self.passengers:
            if passenger.name.strip().casefold() == passenger_name:
                self.passengers.remove(passenger)
                print(f"{passenger.name} ha bajado del autobús.")
                return True

        print("El pasajero no está en el bus.")
        return False


if __name__ == "__main__":
    # Keep asking until the user enters a valid, nonnegative integer capacity.
    print()
    print("Bienvenido al sistema de gestión de pasajeros del autobús.")
    print()
    while True:
        try:
            max_passengers = int(input("Capacidad Máxima del autobús: "))
            bus = Bus(max_passengers) # Create the bus with the specified capacity.
            break
        except ValueError:
            print("La capacidad debe ser un entero mayor o igual a cero.")

    # Read passengers one at a time and enforce the capacity through the bus method.
    print()
    while True:
        print(f"Pasajeros en el autobús: {len(bus.passengers)}/{bus.max_passengers}")
        if len(bus.passengers) >= bus.max_passengers:
            print() 
            print("El bus ya está lleno!.")
            break

        name = input("Nombre del pasajero (Enter para terminar): ").strip()
        if not name:
            break

        # Validate the name before boarding; invalid names do not occupy a seat.
        try:
            person = Person(name)
        except ValueError as error:
            print(error)
            continue

        bus.add_passenger(person)

    # Show the passengers who successfully boarded the bus.
    print("Pasajeros en el bus:", ", ".join(person.name for person in bus.passengers))

    # Let passengers leave one at a time after boarding has finished.
    print()
    while bus.passengers:
        answer = input("Algún pasajero desea bajar? (sí/no): ").strip().casefold()
        if answer == "no":
            break
        if answer not in ("sí", "si"):
            print("Responda sí o no.")
            continue

        name = input("Nombre del pasajero que desea bajar: ").strip()
        try:
            bus.remove_passenger(name)
        except ValueError as error:
            print(error)
            continue

        # Update the passenger count after each departure attempt.
        print(f"Pasajeros en el autobús: {len(bus.passengers)}/{bus.max_passengers}")

    # Show the remaining passengers or indicate that the bus is empty.
    if bus.passengers:
        print("Pasajeros que permanecen en el bus:", ", ".join(person.name for person in bus.passengers))
    else:
        print("No quedan pasajeros en el autobús.")
