# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Please Enter Your password: ")
charInPass = len(password)

if charInPass < 6:
    print("weak")
elif charInPass < 11:
    print("Medium")
elif charInPass  > 10:
    print("Strong")