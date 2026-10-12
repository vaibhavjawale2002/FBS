# convert distance from feet and inches to centimeter and meter
feet = float(input("Enter Feet:"))
inches = float(input("Enter Inches:"))

#convert distance into inches
total_inches = (feet * 12) + inches

#convert inches to centimeter
centimeter = total_inches * 2.54

#convert centimeter to meter
meter = centimeter / 100

#display result
print(f"Distance from {feet} feet and {inches} inches to centimeter is {centimeter} cm")

