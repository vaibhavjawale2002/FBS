#WAP to calculate the percentage of student based on marks of any five suubject
sub1 = float(input("Enter marks of first subject: "))
sub2 = float(input("Enter marks of second subject: "))
sub3 = float(input("Enter marks of third subject: "))
sub4 = float(input("Enter marks of fourth subject: "))
sub5 = float(input("Enter marks of fifth subject: "))

marks_obtained = sub1 + sub2 + sub3 + sub4 + sub5
total_marks =marks_obtained / 500 * 100
# print("Percentage of student is: ", total_marks, "%")
print(f"percentage of student total marks is {total_marks} %")