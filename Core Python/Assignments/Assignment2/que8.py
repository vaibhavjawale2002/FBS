#swap two numbers in third variable

a = int(input("Enter number1:"))
b = int(input("Enter number2:"))


temp = a
a = b       
b = temp

print(f"After swapping number1 is {a} and number2 is {b}")
