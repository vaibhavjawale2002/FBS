# 1.To output are pass the input data.
# 2.Filter() returns a filter object ,commonly convert it to list()
# 3.Any falsy value display in output they considered as False
# falsy = false,0 ,none,blank,' ',[]


data =[1,2,3,4,5,6,7,8,9,10]
res = list(filter(lambda num:num % 2==0, data))
print(res)

# data =[1,2,3,4,5,6,7,8,9,10]
# res = list(filter(lambda num:num*num, data))
# print(res)