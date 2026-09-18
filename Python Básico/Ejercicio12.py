"""
Ejercicio Phyton Basico - One dicttionary from two lists
Student: Cesar Lanuza Urbina
"""

def main():
    # Define two lists of the same size
    keys = ['First_name', 'Last_name', 'Age', 'City']
    values = ['Cesar', 'Lanuza', 57, 'San José']
    
    # Create a dictionary from the two lists using a loop (for)
    student_info = {}
    for i in range(len(keys)):
        student_info[keys[i]] = values[i]
    
    # Print the resulting dictionary
    print()
    print(f"Dictionary: {student_info}")
    print()

    # Print the details of the student in a formatted way
    print()
    print("Detalles del estudiante:", ", ".join([f"'{key}': '{value}'" 
            for key, value in student_info.items()]))
    print()    

if __name__ == "__main__":
    main()
