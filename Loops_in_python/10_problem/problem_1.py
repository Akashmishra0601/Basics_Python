# ques - 1 - counting positive Numbers

numbers = [1,2,3,3,4,5,5,5,-5,4]
positive_number = 0

for num in numbers:
    if num > 0:
        positive_number = positive_number + 1
print(positive_number)