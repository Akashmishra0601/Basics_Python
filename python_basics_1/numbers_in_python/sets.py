# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}


# Adding elements to a set
set1.add(6)
set2.add(8)

# Removing elements from a set
set1.remove(2)
set2.discard(6)

# Set operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

# Other useful methods
set3 = set1.copy()
set3.clear()
popped_element = set1.pop()
length_of_set = len(set1)



# Print results
print("set1:", set1)
print("set2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_difference_set)
print("Copied set (set3):", set3)
print("Popped Element:", popped_element)
print("Length of set1:", length_of_set)