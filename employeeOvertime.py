class Employee:
    def __init__(self, emp_name, emp_ID, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_ID = emp_ID
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_employee_salary(self, hour_worked):
        base_salary = self.emp_salary
        if hour_worked > 50:
            overtime = hour_worked - 50
            overtime_pay = overtime * (base_salary / 50)
            total_salary = overtime_pay + base_salary
        else:
            total_salary = base_salary
        return total_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print('Employee Name:', self.emp_name)
        print('Employee ID:', self.emp_ID)
        print('Employee salary:', self.emp_salary)
        print('Employee department:', self.emp_department)

# Create an empty list to store employee objects
employees = []

# Get employee information from the user
num_employees = int(input("Enter the number of employees: "))

for i in range(num_employees):
    emp_name = input("Enter employee name: ")
    emp_ID = input("Enter employee ID: ")
    emp_salary = float(input("Enter employee salary: "))
    emp_department = input("Enter employee department: ")

    # Create an Employee object and add it to the list
    emp = Employee(emp_name, emp_ID, emp_salary, emp_department)
    employees.append(emp)

# Changing department of an employee:
employees[0].emp_assign_department('Human Resources management')

# Printing employees' details:
for emp in employees:
    emp.print_employee_details()
