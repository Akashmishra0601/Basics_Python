# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

import random
while True:
    petSpecies = random.choice(["Dog", "Cat"])

    if petSpecies == "Dog":
        petsAge = int(input("Enter the value of petAge: "))
        if petsAge < 2:
            print("Puppy food")
        else:
            print("give normal food to your dog")
            
    if petSpecies == "Cat":
        CatsAge = int(input("Enter the value of CatsAge: "))
        if CatsAge < 2:
            print("baby cat food")
        else:
            print("give normal food to your cat")
