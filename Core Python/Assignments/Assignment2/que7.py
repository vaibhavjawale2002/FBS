# find the sum of digits of a three-digit number
num = int(input("Enter a three-digit number: "))

d1 = num%10    #(%) operator to get the last digit
num =num//10   #(//)operator to remove the last digit

d2 = num%10
num =num//10

d3 = num%10
num =num//10

print(num)
