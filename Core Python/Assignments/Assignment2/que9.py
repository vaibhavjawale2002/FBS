#WAP to swap two numbers without using third variable
a = int(input("Enter number1:"))        
b = int(input("Enter number2:"))

a = a + b
b = a - b   
a = a - b
print(f"After swapping number1 is {a} and number2 is {b}")