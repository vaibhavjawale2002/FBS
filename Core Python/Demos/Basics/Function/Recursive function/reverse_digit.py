def reverseDigit(n):
    if(n == 0):
        return
        
    else:
        print(n % 10,end="")  
        reverseDigit(n // 10)
    

num = int(input("Enter number: "))
res = reverseDigit(num)
print(res)