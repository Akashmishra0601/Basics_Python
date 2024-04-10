tea = ["black", "green", "oolong", "white"]

# Accessing the last element of the list
print(tea[-1])

# Slicing the entire list (returns a copy of the list)
print(tea[:])

# Same as above (returns a copy of the list)
print(tea[::])

# Slicing from the second element to the end
print(tea[1:])

# Slicing from the second element to the third element (excluding the third)
print(tea[1:2:])

# Slicing from the second element to the third element with a step of 2
print(tea[1:3:2])

# Slicing the entire list (returns a copy of the list)
print(tea[:5])

# Slicing with a step of 4
print(tea[::4])

# Slicing from the beginning to the third element (excluding the third)
print(tea[:3])

# Modifying the list: Replacing the element at index 3 with "NO"
tea[3] = "NO"
print(tea)

# Modifying the list: Replacing elements from index 1 to 2 with new elements
tea[1:3] = ["jdfjejdvkj", "nvkjnfdk"]
print(tea)

# Appending a new element to the list
tea.append("okay")
print(tea)

# Removing an element using pop (last element by default)
tea.pop()

# Removing an element by value
tea.remove("black")

# Inserting an element at index 1
tea.insert(1, "green")
print(tea)

# Creating a copy of the list (reference change)
tea = tea.copy()

# List comprehension to create a list of squared numbers
squared_nums = [x**2 for x in range(10)]

# List comprehension to create a list of cubed numbers
squared_nums_cubs = [x**3 for x in range(10)]

print(squared_nums_cubs)
print(squared_nums)