Password = input("pls Enter the pass: ")

len_pass = len(Password)
# print(len_pass)

if len_pass < 6:
    print("Your Pass is Week")
elif len_pass < 10:
    print("your pass is medium")
elif len_pass > 10:
    print("your pass is strong")