class Marks:
    def __init__(self):
        self.__math_marks = 0
    def set_math_marks(self, marks):
        if 0<=marks<=100:
            self.__math_marks=marks
        else:
            print("Error: Marks must be between 0 and 100.")
    def display_marks(self):
        print("Math Marks:", self.__math_marks)
stu=Marks()
stu.set_math_marks(90)
stu.display_marks()
stu.set_math_marks(120)
stu.display_marks()
