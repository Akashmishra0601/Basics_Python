# problem - 3

marks = int(input("enter the marks: "))

if marks >=101:
    print("idiot")
    exit()

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("c")
elif marks >= 60:
    print("d")
else:
    print("f")