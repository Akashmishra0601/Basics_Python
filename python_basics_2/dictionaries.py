chai = {
    "masala" : "spicy",
    "ginger" : "zesty",
    "green tea" : "mild",
}

print(chai["masala"])

print(chai.get("gingery"))

chai["ginger"] = "fresh"
print(chai)



for key , value in chai.items():
    print(key , value)

if "masala" in chai:
    print("yes")

print(len(chai))

chai["Earl greay"] = "cirtus"
print(chai)


tea_shop = {
    "chai":{"masala" , "Mild" , "Ginger" , "zesty"},
    "tea" : {"green" , "mild"}
}

tea_shop["chai"]