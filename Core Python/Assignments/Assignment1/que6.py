#write a program to input two angle from user and find the angle of triangle
angle_A = float(input("Enter first angle of triangle: "))
angle_B = float(input("Enter second angle of triangle: "))
angle_C = 180 -(angle_A + angle_B)
print(f"The third angle of triangle is: {angle_C}")