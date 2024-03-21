# # # print("hello everyone")

# # # import os
# # # import sys

# # # print(os.getcwd())
# # # print(sys.platform)


# # # def chai(n):
# # #     print(n)

# # # chai("giner tea")


# # # mutable and immutable
# # # referance matters in python

# # username = "hitesh"
# # username = "chaiaurcode"
# # x_1 = ["heelo" , "cons" ,"erjfrfj", 35]
# # x_2 = x_1
# # print(x_1 , x_2)
# # x_1 = 3
# # print(x_1 , x_2)


# # x = 56
# # y = x
# # print(x ,y)
# # x = 3
# # print(x,y)

# # overview of datatype 
# # datatype shold be same always remember 


# # import math
# # import random

# # b = "hellodhbfvbhbhfjhf"
# # # b[0] = 'a'
# # reverse_str = b[::-1]
# # print(reverse_str)



# # print(math.pi)
# # print(random.random())
# # print(random.randrange(3, 100))
# # print(random.choice(["frhj", "dnfjrbj", "dnvjfkrnj"]))
# # mylist = ["frhj", "dnfjrbj", "dnvjfkrnj", "fbhfrbhfvhbrh", "hfjr4bhj"]
# # random.shuffle(mylist)
# # print(mylist)
# # print(len(b))


# # dict = {'name':"akash",'age':21}
# # dict[0]='namef'
# # print(dict)

# # a = 32
# # b = 54
# # c=54
# # d=c
# # print(a is b)
# # print(c is d)


# # Numbers in python 
# # repr , str , print

# import math
# print(math.floor(3.55))
# print(math.ceil(3.55))
# print(math.trunc(3.55))
# print(bin(655))
# print((655))

# import random
# print(random.randint(3,200))
# print(random.randint(3,6))

# # set = {1,2,3,3}
# # set_1 = {1,3}
# # set_2 = set & set_1
# # set_3 = set | set_1
# # print(set_2)
# # print(set_3)

# strings in python 
str_1 = "123345678987654345"
str_2 = "  akash Mishra    "
list_1 = "dnfhvrbh",'ffnjvrfjn' ,"fhyvvurhffv"

print(str_1[0])
print(str_1[:9])
print(str_1[1:8:2])
print(str_1[::-1])

print(str_2.upper())
print(str_2.lower())
print(str_2.strip())
print(str_2.split())
print(str_2.replace("akash Mishra" , "cfvf"))
print(str_2)


list_1 = "apple,banana,orange"
print(list_1.split(","))  

print(list_1.find("apple"))

chai = ["lemon" , "ginger" , "masala"]
print("-".join(chai))