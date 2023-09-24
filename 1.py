# # 4. Write a program to print the prime numbers within the range given by the user input and 
# # count the prime number and display that number

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def count_and_print_primes_in_range(start, end):
#     count = 0
#     for num in range(start, end + 1):
#         if is_prime(num):
#             count += 1
#             print(num)
#     return count

# if __name__ == "__main__":
#     try:
#         start = int(input("Enter the start of the range: "))
#         end = int(input("Enter the end of the range: "))

#         if start < 0 or end < 0 or start > end:
#             print("Invalid input. Please enter a valid range.")
#         else:
#             prime_count = count_and_print_primes_in_range(start, end)
#             print(f"Number of prime numbers in the range: {prime_count}")
#     except ValueError:
#         print("Invalid input. Please enter valid integers for the range.")

class Teacher:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.__salary = salary  # Using double underscore to make it private

    def show_details_information(self):
        print(f"Mr {self.name}. age {self.age}. Works under department {self.department} and got remuneration of {self.__salary} in PY")

# Function to display the title of Staff Management System
def display_title():
    print("*********Staff Management System**********")
    print("Kathmandu, Nepal")
    
if __name__== "__main__":
    # Input section
    display_title()
    name = input("Enter the name of the Teacher: ")
    age = input("Enter the Age of the Teacher: ")
    department = input("Enter the Department of the Teacher: ")
    salary = input("Enter the Salary of the Teacher: ")

    # Creating a Teacher object
    teacher = Teacher(name, age, department, salary)

    # Output section
    display_title()
    teacher.show_details_information()
