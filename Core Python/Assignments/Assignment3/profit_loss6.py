# WAP to calculate profit or loss
cost_price=float(input("Enter cost price: "))
selling_price = float(input("Enter seling price:"))

if(selling_price > cost_price):
    profit = selling_price - cost_price
    print("Profit is:",profit)
elif(selling_price < cost_price):
    loss = cost_price - selling_price
    print("Loss is:",loss)
else:
    print("No profit, no loss")
