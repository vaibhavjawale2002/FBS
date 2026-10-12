def seprateDigit(n):
    if(num>=0):
        return num%10 
    else:
        return num//10
 
num = int(input('Enter number:'))
res = seprateDigit(num)
print(res)
