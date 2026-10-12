#WAP to convert days into years, weeks and days
days = int(input("Enter number of days: "))
years = days // 365 
remaining_days = days % 365
weeks = remaining_days // 7
remaining_days = remaining_days % 7
print(f"Years: {years}")
print(f"Weeks: {weeks}")
print(f"Days: {remaining_days}")