class Student:
    def __init__(self):
        self.__name = ""
        self.__marks = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Error: Marks should be between 0 and 100.")

    def get_marks(self):
        return self.__marks

# Main code
student = Student()
# User input
name=input("Enter Your Name:")
student.set_name(name)
student.set_marks(100)
student.set_name(name)
marks = int(input("Enter student marks (0-100): "))
student.set_marks(marks)

# Output
print("\nStudent Name:", student.get_name())
print("Student Marks:", student.get_marks())

# Try setting invalid marks
student.set_marks(150)
print("\nStudent Name:", student.get_name())