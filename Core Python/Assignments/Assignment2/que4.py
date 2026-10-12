base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

#calculate area of triangle
area = 0.5 * base * height

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

#calculate area of rectangle
area_rectangle = length * width

#display result
print(f"Area of the triangle with base {base} and height {height} is {area}")
print(f"Area of the rectangle with length {length} and width {width} is {area_rectangle}")