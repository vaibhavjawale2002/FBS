# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random


userid = input("Enter your user id: ")
password = input("Enter your password: ")

if (userid == "vaibhav" and password == "vaibhav@26"):
    captcha = random.randint(1000, 9999)
    print("Captcha is:", captcha)
    num = int(input("Enter the captcha: "))
    if (num == captcha):
        print("Successful login")
    else:
        print("Login failed")
