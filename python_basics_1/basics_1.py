print("Hello Everyone")

Number_1 = int(input("Enter The value of Number_1: "))
Number_2 = int(input("Enter The value of Number_2: "))

Result = Number_1 + Number_2
# print(`Numner_1 + Number_2 = ${Result}`) # in javascript
print(f'Number_1 + Number_2 = {Result}') 

def addTwoNumbers(Number_1 , Number_2): #parameters
    result = Number_1 + Number_2
    return result

print(addTwoNumbers(456 , 4)) # arguments
ResultOf = addTwoNumbers(45 , 6)
print(f'reult = {ResultOf}')

def chai(n):
    print(n)

chai(4)
chai("lemon tea")
chai("masala chai")


    # modules in python:
    #     os , sys , importlib , reload , platform , cwd

import os 
import sys 


os_path = os.getcwd()
print(f"os_path = {os_path}")

system_plateform = sys.platform
print(f"system_plateform = {system_plateform}")
