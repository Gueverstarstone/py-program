languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:                         # Loop through each language in the list
    print(f'Index {index} and language {language}')# Prints index and language
    index += 1                                     # Manually increment index
# Output:
# Index 0 and language Spanish
# Index 1 and language English
# Index 2 and language Russian
# Index 3 and language Chinese


languages = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages)))                  # Converts enumerate object into list of tuples
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]
# Each entry is a tuple: (index, value)


# Refactor using enumerate (no need for manual index variable)
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):       # enumerate gives both index and value
    print(f'Index {index} and language {language}')
# Output:
# Index 0 and language Spanish
# Index 1 and language English
# Index 2 and language Russian
# Index 3 and language Chinese


# Using enumerate with a custom start index
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages, 1):    # Start counting from 1 instead of 0
    print(f'Index {index} and language {language}')
# Output:
# Index 1 and language Spanish
# Index 2 and language English
# Index 3 and language Russian
# Index 4 and language Chinese


developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))                  # Pairs elements from both lists into tuples
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]


# Using zip() in a for loop
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):              # Iterates over paired values
    print(f'Name: {name}')                         # Prints developer name
    print(f'ID: {id}')                             # Prints corresponding ID
# Output:
# Name: Naomi
# ID: 1
# Name: Dario
# ID: 2
# Name: Jessica
# ID: 3
# Name: Tom
# ID: 4
