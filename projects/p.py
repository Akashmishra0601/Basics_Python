# enumerate 
x = ('Akash' , 'Bkash' , "ckash" , "dkash")
y = enumerate(x)
print(y)

print(list(y))

file = open('text.py' , 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

with open('youtube.txt' , 'w') as file:
    file.write('chai aur python')