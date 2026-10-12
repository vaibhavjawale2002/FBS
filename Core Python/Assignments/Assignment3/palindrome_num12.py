# Write a program to check if given 3 digit number is a palindrome or not.
# num = int(input("Enter a 3-digit number: "))
# original_num = num
# reverse_num = 0
# while (num > 0):
#     digit = num % 10
#     reverse_num = reverse_num * 10 + digit
#     num = num // 10
# if (original_num == reverse_num):
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")

num = int(input("Enter a 3-digit number: "))

if num > 0:

    num1 = num // 100
    num2 = (num // 10) % 10
    num3 = num % 10

    if num1 == num3:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")

else:
    print("Please enter a 3-digit number.")

