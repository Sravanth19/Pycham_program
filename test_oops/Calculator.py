class Calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def multi(self, a, b):
        return a*b
    def divi(self, a, b):
        if b==0:
            return "Error: Division by zero is not allowed."
        return a/b
cal=Calculator()

num1=float(input("Enter the 1st num: "))
num2=float(input("Enter the 2nd num: "))

print("Addition: ({} - {}): {}".format(num1, num2, cal.add(num1, num2)))
print("Subtraction ({} - {}): {}".format(num1, num2, cal.sub(num1, num2)))
print("Multiplication ({} * {}): {}".format(num1, num2, cal.multi(num1, num2)))
print("Division ({} / {}): {}".format(num1, num2, cal.divi(num1, num2)))
