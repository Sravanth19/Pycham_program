def divide(a, b):
    try:
        result = a / b
        return print(result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")
a=int(input("Enter the numerator:"))
b=int(input("Enter the denominator:"))

divide(a,b)