# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
total = 0 
for i in range(1, 6):
    age = int(input("Enter your age: "))
    tkt_amt= float(input("Enter ticket amount: "))
    if (age < 12):
        tkt_amt = tkt_amt - (tkt_amt * 0.3)
        # total_amt = tkt_amt - discount
        # print("Total amount to pay after 30% discount is:", total_amt)
    elif (age > 59):
        tkt_amt = tkt_amt - (tkt_amt * 0.5)
        # total_amt = tkt_amt - discount
        # print("Total amount to pay after 50% discount is:", total_amt)
    total = total + tkt_amt
print("Total amount to pay for all 5 people is:", total)