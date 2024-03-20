
distance = int(input("enter distance:  "))

if distance < 3:
    print("go walk")
elif distance < 15:
    print("Bike")
elif distance > 15:
    print("car")