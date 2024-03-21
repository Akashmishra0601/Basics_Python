score = int(input("enter the score: "))

if score > 100:
    print("idiot")
    exit()

if score >= 90:
    print("a")
elif score >= 80:
    print("b")
elif score >= 70:
    print("c")
elif score >= 60:
    print("d")
else:
    print("f")