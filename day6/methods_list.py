names = ['wantam', 'mungai', 'zuri', ['dedan', 'nyawi']]
numbers = [1, 2, 3, 4]

# Extending 'names' with 'numbers'
names.extend(numbers)             # Adds each element of 'numbers' to the end of 'names'
# names → ['wantam','mungai','zuri',['dedan','nyawi'],1,2,3,4]

# Inserting 3.5 at position 3 in 'numbers'
numbers.insert(3, 3.5)            # Inserts 3.5 at index 3
# numbers → [1,2,3,3.5,4]

# Extending 'names' with another item ['kinuthia']
names.extend(['kinuthia'])        # Adds 'kinuthia' to the end of 'names'
# names → [...,4,'kinuthia']

# Appending 'kigonyi' to 'names'
names.append('kigonyi')           # Adds 'kigonyi' as the last element
# names → [...,'kinuthia','kigonyi']

# Printing the lists
print(names)                      # ['wantam','mungai','zuri',['dedan','nyawi'],1,2,3,4,'kinuthia','kigonyi']
print(numbers)                    # [1,2,3,3.5,4]

# Removing the number 4 from 'numbers'
numbers.remove(4)                 # Removes the first occurrence of 4
# numbers → [1,2,3,3.5]

# Printing after removal
print(numbers)                    # [1,2,3,3.5]

# Popping the element at index 1 from 'numbers'
numbers.pop(1)                    # Removes element at index 1 → 2
# numbers → [1,3,3.5]

# Printing after popping
print(numbers)                    # [1,3,3.5]

numbers2 = [34,67,423,87,346,5767,215,56]
numbers2.sort()                   # Sorts the list in place (ascending order)
print(numbers2)                   # [34,56,67,87,215,346,423,5767]

numbers3 = [23,5,76,3,25,78,9]
new_numbers = sorted(numbers3)    # Returns a new sorted list (original unchanged)
print(new_numbers)                # [3,5,9,23,25,76,78]

numbers4 = [23,5,76,3,25,78,9]
numbers4.reverse()                # Reverses the list in place
print(numbers4)                   # [9,78,25,3,76,5,23]

programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(programming_languages.index('Java')) # Finds the index of 'Java' → 1
