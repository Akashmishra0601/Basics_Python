# # ques-2
# movie ticket price:

day_wednesday = input("enter the day(yes/no): ")
age = int(input("enter the age: "))

ticket_price = 0
if day_wednesday == "yes":
    if age >= 18:
        ticket_price = 12
    elif age < 18:
        ticket_price = 8
        
    print(ticket_price - 2)

else:
    if age >= 18:
        ticket_price = 12
    elif age < 18:
        ticket_price = 8
    print(ticket_price)
