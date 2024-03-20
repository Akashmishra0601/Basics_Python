import random

# Seed random number generator (optional)
random.seed(42)

# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)

# Generate a random float between 0 and 1
random_float = random.random()

# Generate a random integer from a range (start, stop, step)
random_range = random.randrange(1, 100, 2)  # Start from 1, end at 99, step by 2

# Generate a random choice from a sequence
options = ["apple", "banana", "cherry", "date"]
random_choice = random.choice(options)

# Shuffle a sequence in place
sequence = [1, 2, 3, 4, 5]
random.shuffle(sequence)


# Print results
print("Random Integer:", random_integer)
print("Random Float:", random_float)
print("Random Range:", random_range)
print("Random Choice:", random_choice)
print("Shuffled Sequence:", sequence)