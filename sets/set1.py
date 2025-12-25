my_num ={1,2,3,4,5,6,7}
my_num.add(8)
my_num.remove(7)
print(my_num)
my_num = set({})
my_num.add(8)
print(my_num)


# -------------------------------
# Set 1: Creating sets
# -------------------------------
# Create a set with curly braces
fruits = {"apple", "banana", "cherry"}

# Create a set from a list using set()
numbers = set([1, 2, 3, 3, 2, 1])  # duplicates are removed
print(fruits)    # {'apple', 'banana', 'cherry'}
print(numbers)   # {1, 2, 3}


# -------------------------------
# Set 2: Adding and removing elements
# -------------------------------
colors = {"red", "blue"}

# Add a new element
colors.add("green")

# Remove an element (raises error if not found)
colors.remove("blue")

# Discard an element (no error if not found)
colors.discard("yellow")

print(colors)   # {'red', 'green'}


# -------------------------------
# Set 3: Set operations (union, intersection, difference)
# -------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: combine elements
print(A | B)   # {1, 2, 3, 4, 5, 6}

# Intersection: common elements
print(A & B)   # {3, 4}

# Difference: elements in A but not in B
print(A - B)   # {1, 2}

# Symmetric difference: elements in either A or B but not both
print(A ^ B)   # {1, 2, 5, 6}


# -------------------------------
# Set 4: Membership and iteration
# -------------------------------
animals = {"dog", "cat", "lion"}

# Check membership
print("dog" in animals)        # True
print("tiger" not in animals)  # True

# Loop through set
for animal in animals:
    print(animal)


# -------------------------------
# Set 5: Useful methods
# -------------------------------
numbers = {1, 2, 3}
numbers.update([4, 5])   # add multiple elements
print(numbers)           # {1, 2, 3, 4, 5}

numbers.clear()          # remove all elements
print(numbers)           # set()


# -------------------------------
# Set 6: Frozen sets (immutable sets)
# -------------------------------
frozen = frozenset([1, 2, 3, 3])
print(frozen)            # frozenset({1, 2, 3})

# frozen.add(4)  # ❌ Error: frozenset is immutable
