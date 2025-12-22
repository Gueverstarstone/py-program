# lists
names = ['wantam','mungai','zuri',['dedan','nyawi']]
names[1] = 'zuriel'              # Replace 'mungai' with 'zuriel'
print(names[-1])                 # Prints the last element → ['dedan','nyawi']
print(len(names))                # Prints length of list → 4
print(names)                     # Prints full list → ['wantam','zuriel','zuri',['dedan','nyawi']]
del names[1]                     # Deletes element at index 1 ('zuriel')
print(names)                     # Prints updated list → ['wantam','zuri',['dedan','nyawi']]
print('wantam' in names)         # Checks membership → True
print(names[2][0])               # Access nested list → 'dedan'

# list()
place = 'elementaita'
print(list(place))               # Converts string into list of characters → ['e','l','e','m','e','n','t','a','i','t','a']

# Unpacking values
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer       # Unpacks list into variables
print(name)                      # 'Alice'
print(age)                       # 34
print(job)                       # 'Rust Developer'

# Example: unpacking a list of fruits using the asterisk (*) operator
fruits = ['Mango', 'Banana', 'Orange', 'Pineapple']
first, *others = fruits          # 'first' gets first element, 'others' gets the rest
print(first)                     # 'Mango'
print(others)                    # ['Banana', 'Orange', 'Pineapple']

# slice operator (:)
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4]                    # Slice from index 1 up to (but not including) 4 → ['Cookies','Ice Cream','Pie']

# how slicing with a step interval works in Python.
numbers = [1, 2, 3, 4, 5, 6]

print(numbers[::2])              # Odd numbers → [1, 3, 5] (start at index 0, step by 2)
print(numbers[1::2])             # Even numbers → [2, 4, 6] (start at index 1, step by 2)
print(numbers[2:5:2])            # Slice from index 2 to 4, step 2 → [3, 5]
print(numbers[::-1])             # Reverse list → [6, 5, 4, 3, 2, 1]
