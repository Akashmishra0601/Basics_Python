# 9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# The condition for a leap year in Python is:

# If the year is evenly divisible by 4,
# And if the year is not evenly divisible by 100,
# Or if the year is evenly divisible by 400.

check_Year = 2020

if (check_Year % 400 == 0) or ((check_Year % 4 == 0) and (check_Year % 100 != 0)):
    print("yes year is leap year")
else:
    print("no")