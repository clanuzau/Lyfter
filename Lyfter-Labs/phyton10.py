"""
Ejercicio - Python Basic - Control de notas
Student: Cesar Lanuza Urbina
"""
def main():
# Variables inizialization
    total_grades                        = 0
    grade_counter                       = 1
    current_grade                       = 0
    number_of_passed_grades             = 0
    number_of_failed_grades             = 0
    average_of_approved_grades          = 0
    average_of_failed_grades            = 0 
    average_of_total_grades             = 0

    total_grades = input('Ingrese la cantidad de notas: ').strip()

    while not total_grades.isdigit():
        total_grades = input('Ingrese una cantidad valida de notas: ').strip()

    total_grades = int(total_grades)

    while grade_counter <= total_grades:
        current_grade = input(f'Ingrese la nota numero {grade_counter}: ').strip()

        while not current_grade.isdigit():
            current_grade = input(f'Ingrese una nota valida para la nota numero {grade_counter}: ').strip()

        current_grade = int(current_grade)
        average_of_total_grades += current_grade

        if current_grade < 70:
            number_of_failed_grades += 1
            average_of_failed_grades += current_grade
        else:
            number_of_passed_grades += 1
            average_of_approved_grades += current_grade

        grade_counter += 1

    average_of_total_grades = average_of_total_grades / total_grades

    if number_of_failed_grades > 0:
        average_of_failed_grades = average_of_failed_grades / number_of_failed_grades

    if number_of_passed_grades > 0:
        average_of_approved_grades = average_of_approved_grades / number_of_passed_grades

    print(" ")
    print("El estudiante tiene esta cantidad de notas:")
    print(f'Notas aprobadas: {number_of_passed_grades}')
    print(f'Promedio de notas aprobadas: {average_of_approved_grades:0f}')
    print(" ")
    print(f'Notas reprobadas: {number_of_failed_grades}')
    print(f'Promedio de notas reprobadas: {average_of_failed_grades}')
    print(" ")
    print(f'Promedio total de notas: {average_of_total_grades}')

    
if __name__ == "__main__":
    main()