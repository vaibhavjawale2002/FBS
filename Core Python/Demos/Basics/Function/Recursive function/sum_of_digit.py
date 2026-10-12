def sumOfDigit(num):
    if(num==0):
        return 0
    
    return (num%10)+sumOfDigit(num//10)

    
num =int(input("Enter number:"))
res= sumOfDigit(num)
print(res)  