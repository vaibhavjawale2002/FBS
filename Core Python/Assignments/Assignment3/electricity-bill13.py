# Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill.

ele_unit = float(input("Enter electricity unit charges: "))

if (ele_unit <= 50):
    bill = ele_unit * 0.50
elif (ele_unit <= 100):
    # bill = ele_unit * .075
    bill = (50 * 0.50) + ((ele_unit - 50) * 0.75)
elif (ele_unit <= 250):
    # bill = ele_unit * 1.20
    bill = (50 * 0.50) + (100 * 0.75) + ((ele_unit - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((ele_unit - 250) * 1.50)

# Apply surcharge
bill = bill + (bill * 0.20)

print("Total electricity bill is:", bill)