# Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: ")) 
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: ")) 
sub5 = int(input("Enter marks of subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
avg = total / 5
print("Total marks:", total)
print("Average marks:", avg)


if(avg >= 90):
    print("Distinction...Best of luck for future.")
elif(avg >= 80):
    print("First Class")
elif(avg >= 60):
    print("Second Class")
elif(avg >= 40):
    print("Third Class")
else:
    print("Fail...Better luck next time.")