
order_size = "medium"
extra_shot = False

if extra_shot:
    coffee = order_size + "coffee with an extra shot"
else:
    coffee = order_size + "coffee "

print("order: " , coffee)