# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

import random

weather = random.choice(["Sunny", "Rainy", "Snowy"])

if weather == "Sunny":
    print("Go for a walk")
elif weather == "Rainy":
    print("Read a book")
elif weather == "Snowy":
    print("Build a snowman")