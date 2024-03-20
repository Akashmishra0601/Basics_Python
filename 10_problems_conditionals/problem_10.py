
pet_species = input("Enter the pet_species: ")
pet_age = int(input("enter th pet_age: "))

if pet_species == "Dog":
    if pet_age < 5:
        print("give baby food")
    else:
        print("Giev senior food")
elif pet_species == "cat":
    if pet_age < 2:
        print("give baby food")
    else:
        print("Giev senior food")
else:
    print("Idiot write first latter capital")
