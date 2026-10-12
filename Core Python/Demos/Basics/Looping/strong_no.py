num = int(input('Enter number:'))
temp_num = num
sum = 0
while(num>0):
    d = num%10
    num = num//10
    # print(d)
    multi = 1
    for i in range(1, d+1):
        multi*=i
        # print(multi)    
    sum += multi
    
if(sum == temp_num):
    print(f'{temp_num} the number is strong number')
else:
    print(f'{temp_num} the number is not strong number')