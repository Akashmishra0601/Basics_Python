dist = {"masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(dist["masala"])

print(dist.get("Ginger"))

dist["Green"] = "Fresh"

print(dist)

for chai in dist:
    print(chai, dist[chai])

for key, value in dist.items():
    print(key,value)

if "masala" in dist:
    print("yes")

print(len(dist))

dist["erl grey"] = "citrus"
print(dist)

dist.pop("Ginger")
print(dist)

dist.popitem()
print(dist)

del dist["Green"]
print(dist)

dist = dist.copy()

t_shop = {"chai": {"Masala": "Spicy", "Ginger": "Zesty", "over": "recall"}}