# leap year 

year = 2026

if (year % 400 == 0) or (year % 4 == 0 and year != 0):
    print(year ,"is a leap year")
else:
    print("not a leap year")