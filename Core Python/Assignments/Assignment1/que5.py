# WAP to enter P,T, and calculate compound interest
P = float(input("Enter principal amount: "))
T = float(input("Enter time in years: "))   
R = float(input("Enter rate of interest: "))
CI = P * (1 + R / 100) ** T - P
print(f"Compound Interest for principal amount {P}, time {T} years and rate of interest {R}% is: {CI}")