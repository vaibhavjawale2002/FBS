# convert time entered in hh,mm,ss into seconds
Hour = int(input("Enter hour: "))
Minute = int(input("Enter minute: "))       
Second = int(input("Enter second: ")) 

# perform operation

Total_seconds = (Hour * 3600) + (Minute * 60) + Second

# display result
print(Total_seconds)
print(f"Total seconds in {Hour} hour, {Minute} minute and {Second} second is {Total_seconds}")
