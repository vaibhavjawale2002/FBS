# 1.To neglect positional parameter concept.
# 2.Assign value to parameter in function call.
# 3.Name of parameter in function call and function defination should be same 
# 4.flow from right to left
def emp(id, name, sal, dept):
    return f"ID:{id}\nNAME:{name}\nSALARY:{sal}\nDEPARTMENT:{dept}"
# res= emp(5000,"ABC","IT",101)
res= emp(sal=5000,name="ABC",dept="IT",id=101)#assign to the keywords 
print(res)