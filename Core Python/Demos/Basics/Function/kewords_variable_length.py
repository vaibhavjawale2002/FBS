# 1.To pass multiple values with meaning
# 2.mention 2 Astrisk(star) symbol before pass parameter name in fd
# 3.values and meaning stored in dictionary format
# 4.use for loop an dict.items() to iterate data.
def emp(**data):
    # for i in data.items():
    for key ,val in data.items():
        # print(i)
        print(key,":",val)
emp(id=101, name="ABC", sal=150, dept= "IT")