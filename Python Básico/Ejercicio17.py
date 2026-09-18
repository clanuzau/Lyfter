"""
Task Phyton Basico - Create two functions. One of them call to the other.
Student: Cesar Lanuza Urbina
"""

def main():

# Function to calculate total salary

# Function salary is calling function overtime_pay   
    def salary(salary_amount, bonus_amount, hours_worked, hourly_rate):
        total_salary = salary_amount + bonus_amount + overtime_pay(hours_worked, hourly_rate)
        return total_salary
    

# Function to calculate overtime pay
    def overtime_pay(hours_worked, hourly_rate):
        overtime_amount = (hourly_rate * hours_worked) *  1.5
        return overtime_amount


# Function to calculate average salary
    def average_salary(salaries):
        average = sum(salaries) / len(salaries)
        return average  
    
# Collecting salary and bonus details for employees
    total_salaries = []

    print()
    while True:
        try:
            employee_count = int(input("Enter the number of employees: "))
            if employee_count > 0:
                break
        except ValueError:
            pass
        print("Enter a positive number of employees.")

# Loop to get salary and bonus for each employee
    for i in range(employee_count):
        print()
        print(f"Enter the details for employee {i + 1}:")
        print()
        salary_amount = float(input("Enter the salary : "))
        bonus_amount = float(input(" Enter the bonus  : "))
        hours_worked = float(input(" Hours worked     : "))
        hourly_rate = (salary_amount/40) # Assuming salary plus bonus is for a standard 40-hour work week
        overtime_hours = max(0, hours_worked - 40)
        overtime_amount = overtime_pay(overtime_hours, hourly_rate)

# Calculating total salary for the employee. Using function salary which is calling function overtime_pay
        total_salary = salary(salary_amount, bonus_amount, overtime_hours, hourly_rate)

# Appending the total salary to the list of total salaries
        total_salaries.append(total_salary)
        
# Displaying the salary details for the employee
        print()
        print(f"Salary amount   : {salary_amount:.2f}")
        print(f"Bonus amount    : {bonus_amount:.2f}")
        print(f"Hourly rate     : {hourly_rate:.2f}")
        print(f"Overtime hours  : {overtime_hours:.2f}")
        print(f"Overtime pay    : {overtime_amount:.2f} = ({overtime_hours:.2f} * {hourly_rate:.2f} * 1.5)")
        print(f"Total salary    : {salary_amount:.2f} + {bonus_amount:.2f} + {overtime_amount:.2f} = {total_salary:.2f}")
        print()
        print(f">>The total salary for employee {i +1} is: {total_salary:.2f}\n")
        print()

# Calculating the average salary
    average = average_salary(total_salaries)

# Displaying the average salary
    print()
    print(f">>The average salary is: {average:.2f}")
    print()

if __name__ == "__main__":
    main()
