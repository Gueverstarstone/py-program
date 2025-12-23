# Tuple
my_tuple = (1,2,'munga')
print(my_tuple)                  # Prints the whole tuple → (1, 2, 'munga')
print(my_tuple[1])               # Prints element at index 1 → 2

my_name = 'WANTAM'
print(tuple(my_name))            # Converts string into tuple of characters → ('W','A','N','T','A','M')

developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer       # Unpacks tuple into variables
print(name)                      # 'Alice'
print(age)                       # 34
print(job)                       # 'Rust Developer'

developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer          # 'name' gets first element, 'rest' gets the remaining elements
print(name)                      # 'Alice'
print(rest)                      # [34, 'Rust Developer']

# methods
name = ('Munga','wantam','zuri','Munga','Kinuthia','wantam')
# If no arguments are passed into the count() function, then Python raises a TypeError:
print(name.count('Munga'))       # Counts occurrences of 'Munga' → 2
# If the specified item cannot be found, then Python raises a ValueError:
print(name.index('zuri'))        # Finds index of 'zuri' → 2

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3)) # 5
# Starts searching for 'Python' at index 3 → finds it at index 5 (not the earlier one at index 2)

# You can also pass in an optional stop index
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(programming_languages.index('Python', 2, 5)) # 2
# Search starts at index 2 and stops before index 5 → finds 'Python' at index 2

# Sorting with key argument (by length of string)
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, key=len))
# Sorts items by length → ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

# Sorting in reverse order
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages, reverse=True))
# Sorts alphabetically in descending order → ['Rust','Rust','Python','Python','Java','C++']
# Adding reverse=True flips the order to descending.
# So instead of A → Z, you get Z → A.