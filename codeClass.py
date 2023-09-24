class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        base_salary = self.emp_salary
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_pay = overtime * (base_salary / 50)
            total_salary = base_salary + overtime_pay
        else:
            total_salary = base_salary
        return total_salary

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print('Employee Name:', self.emp_name)
        print('Employee ID:', self.emp_id)
        print('Employee Salary:', self.emp_salary)
        print('Employee Department:', self.emp_department)


# Sample Employee Data
employee1 = Employee("RAHUL", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("PRAKASH", "E7499", 45000, "RESEARCH")
employee3 = Employee("ADAM", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

# Changing the department of an employee
employee1.assign_department("HUMAN RESOURCES")

# Printing employee details
print("Employee 1 Details:")
employee1.print_employee_details()
print("\nEmployee 2 Details:")
employee2.print_employee_details()
print("\nEmployee 3 Details:")
employee3.print_employee_details()
print("\nEmployee 4 Details:")
employee4.print_employee_details()

# Calculate salary with overtime for Employee 1
hours_worked = 55  # Example: Employee 1 worked 55 hours
total_salary = employee1.calculate_emp_salary(hours_worked)
print(f"\nTotal Salary for Employee 1 with overtime: {total_salary}")
