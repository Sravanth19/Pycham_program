class Employee:
    def __init__(self):
        self.__name = ""
        self.__salary = 0.0
        self.__age = 0

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for salary with validation
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Error: Salary must be greater than 0.")

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for age with validation
    def set_age(self, age):
        if 18 <= age <= 100:
            self.__age = age
        else:
            print("Error: Age must be between 18 and 100.")

    # Getter for age
    def get_age(self):
        return self.__age

    # Display method
    def display_info(self):
        print("\nEmployee Details:")
        print("Name:", self.get_name())
        print("Salary:", self.get_salary())
        print("Age:", self.get_age())

# Main code with user input
emp = Employee()
name = input("Enter employee name: ")
emp.set_name(name)
try:
    salary = float(input("Enter employee salary: "))
    emp.set_salary(salary)
except ValueError:
    print("Invalid input. Salary must be a number.")
try:
    age = int(input("Enter employee age: "))
    emp.set_age(age)
except ValueError:
    print("Invalid input. Age must be a number.")

