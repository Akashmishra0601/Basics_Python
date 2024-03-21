items = ["apple " , "Hello " , "Hello " ," sets"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("duplecate:" , item)
        break
    unique_item.add(item)
