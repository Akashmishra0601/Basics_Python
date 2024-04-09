# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.


day = input("Enter day: ")
age = int(input("Enter your age: "))

if day == "wednesday":
    if age >= 18:
        print("Ticket price is 10 $")
    elif age < 18:
        print("Ticket price is 6 $")

else:
    if age >= 18:
        print("Ticket price is 10 $")
    elif age < 18:
        print("Ticket price is 6 $")