# problem - 1 - age group categorization 

age = int(input("Pls Enter Age: \n"))

if age < 13:
    print("child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("senior")