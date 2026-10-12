def sumOfSeries(n):
    if(n <= 0):
        return 0
    else:
        return n + sumOfSeries(n - 1)
num = int(input("Enter number: "))
res = sumOfSeries(num)
print(res)
