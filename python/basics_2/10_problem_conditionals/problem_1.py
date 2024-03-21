# # ques -1 
# age group classification:

age = int(input("Enter the age: "))

if age < 13:
    print("child")
elif age < 20:
    print("teenager")
elif age < 60:
    print("adult")
elif age >= 60:
    print("senior")