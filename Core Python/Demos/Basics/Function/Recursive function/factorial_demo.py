#calculate factorial

def factorial(n):
    if (n<=1):
        return 1
    else:
        return n*factorial(n-1)
    
num =int(input("Enter number:"))
res= factorial(num)
print(res)  