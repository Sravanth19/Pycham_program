name=input("Enter your full name:")
age=int(input("Enter your age:"))
print("Hello, "+ name +"! You will be "+ str(age + 5) +" years old in 5 years.")


nums=[]
print("Enter 5 numbers:")
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    nums.append(num)
print("\nNumbers in reverse order:")
print(nums[::-1])
total=sum(nums)
average = total / len(nums)
print(f"Sum of the numbers: {total}")
print(f"Average of the numbers: {average}")
