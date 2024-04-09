# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

import random
fruit = "Banana"
fruitColour = random.choice(["Green", "yellow", "Brown"])
# print(fruitColour)


if fruit == "Banana":
    if fruitColour == "Green":
        print("Unripe")
    elif fruitColour == "Yellow":
        print("Unripe")
    elif fruitColour == "Brown":
        print("Overripe")