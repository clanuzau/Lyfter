"""
Student : Cesar Lanuza Urbina
Program : Employee encapsulation with properties and salary validation.
"""

# Define the Employee class with encapsulated attributes and validation.
class Employee:
    # Initialize the attributes through their setters.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Return the employee name.
    @property
    def name(self):
        return self._name

    # Store the name in the private-by-convention attribute.
    @name.setter
    def name(self, value):
        self._name = value

    # Return the employee salary.
    @property 
    def salary(self):
        return self._salary

    # Validate the salary before updating the stored value.
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salary = value

    # Apply a salary increase using a decimal rate (0.1 means 10%).
    def promote(self, percentage):
        if percentage < 0:
            raise ValueError("El porcentaje de aumento no puede ser negativo.")
        self.salary = self.salary * (1 + percentage)


def main():
    # Create an employee and display both public properties.
    employee = Employee("Ana", 1000)
    print()
    print(f"Nombre: {employee.name}")
    print(f"Salario inicial: {employee.salary:g}")
    print(f"Aumento del 10%: {employee.salary * 0.1:g}")

    # Increase the salary by 10% and display the result: 1100.
    employee.promote(0.1)
    print(f"Salario despues del aumento: {employee.salary:g}")
    print()

   

# Execute the example only when running this file directly.
if __name__ == "__main__":
    main()