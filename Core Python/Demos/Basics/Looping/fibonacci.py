n = int(input("How many fibonacci number:"))

a = -1
b = 1
for i in range(n):
    c= a+b
    print(c)
    # print(c, end = '')
    a=b
    b=c