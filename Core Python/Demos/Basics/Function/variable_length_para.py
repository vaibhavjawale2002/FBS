# 1.To pass multiple para of function
# 2.mention 1 astrisk(star) before para name in function defination
# 3.values are stored in tuple format
# 4.use for loop to iterate values individually from tuple.
def add(*data):
    sum = 0
    for val in data:
        sum+=val
    return sum
res = add(10,20,30,40,1,2,3,4,5)
print(res)