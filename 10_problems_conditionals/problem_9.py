leap_year = 2024

if (leap_year % 400 == 0) or (leap_year % 4 == 0) and (leap_year % 100 != 0):
    print(leap_year , " is a leapyear")
else:
    print("give another")