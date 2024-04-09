# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.


import random
coffeeOrder = random.choice(["Small", "Medium", "Large"])

if coffeeOrder == "Small":
    extraShot = int(input("is u want to add etra shot/ pls Enter 1: "))
    if extraShot == 1:
        print("Your order is : Small with extra shot")
    else:
        print("Your order is : Small")

if coffeeOrder == "Medium":
    extraShot = int(input("is u want to add etra shot/ pls Enter 2: "))
    if extraShot == 2:
        print("Your order is : Medium with extra shot")
    else:
        print("Your order is : Medium")

if coffeeOrder == "Large":
    extraShot = int(input("is u want to add etra shot/ pls Enter 3: "))
    if extraShot == 3:
        print("Your order is : Large with extra shot")
    else:
        print("Your order is : Large")