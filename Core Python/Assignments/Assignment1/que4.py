# WAP to enter P.T.R and calculate simple interest
P = float(input("Enter principal amount: "))
T = float(input("Enter time in years: "))
R = float(input("Enter rate of interest: "))
SI = (P * T * R) / 100
print(f"Simple Interest for principal amount {P}, time {T} years and rate of interest {R}% is: {SI}")