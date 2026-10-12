# 1.To make prameter optional
# 2.Assign value of parameter to function defination
# 3.If we pass value to default parameters,it takes passed Value
#     if we don't pass value to default parameters,it take default value
# 4.flow from right to left
def emp(id, name ="abc", sal=10000, dept= "Back office"):
    print("ID:", id)
    print("NAME:", name)
    print("SAlARY:", sal)
    print("DEPARTMENT:", dept)
    print("###")
emp(101, "ABC", 20000)
# emp(102, "XYZ", 20000,"IT")
