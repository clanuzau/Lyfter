"""
Ejercicio Phyton Basico - Employees by department
Student: Cesar Lanuza Urbina
"""


def main():

    result = {}

    employees = [
        {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
        {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
        {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
        {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
        {"name": "Cesar", "email": "cesar@empresa.com", "department": "TI"},
        {"name": "Diana", "email": "diana@empresa.com", "department": "RRHH"},
        {"name": "Gail", "email": "gail@empresa.com", "department": "Ventas"},
        {"name": "Maria", "email": "maria@empresa.com", "department": "TI"},
        {"name": "Mario", "email": "mario@empresa.com", "department": "TI"},
    ]


    # Create a dictionary to store employees by department
    for employee in employees:
        department = employee['department']

        if department not in result:
            result[department] = []

        result[department].append(employee)

    print()
    print("Employees by department:")
    print()

    for department, department_employees in result.items():
        print(f"{department}:")

        for employee in department_employees:
            print(f"  {employee['name']} - {employee['email']}")

        print()

    print("Result dictionary:")
    print()
    print(result)
    print()


if __name__ == "__main__":
    main()
