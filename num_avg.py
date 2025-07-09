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