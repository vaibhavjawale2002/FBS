# WAP to calculate selling price of book based on cost price and discount
CP = float(input("Enter cost price:"))
Discount = float(input("Enter discount percentage:"))
#calculate discount amount
discount_amount = (CP * Discount) / 100
#calculate selling price    
SP = CP - discount_amount
#display result     
print(f"The discount amount of book is {discount_amount} and final selling priceof book is {SP}")