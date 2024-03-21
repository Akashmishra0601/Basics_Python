# List 

array_1 = ["Akash" , "Ravi" , "Ayush" ,"Ankit"]
array_2 = ["India" , " bangladeesh" , "shrilanka"]

print(array_1[:])
print(array_1[0:2])
print(array_1[2:])
print(array_1[:4])
print(array_1[0:3:2])

array_1.append(array_2)
print(array_1)

# array_1.clear()
# print(array_1)

array_1.insert(2 , "Akash")
print(array_1)

print(range(0,10))

# comprehension 
squared_num = [x**2 for x in range(10)]
print(squared_num)

cube_num = [y**3 for y in range(0,5)]
print(cube_num)