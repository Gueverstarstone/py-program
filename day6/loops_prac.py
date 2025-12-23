# Simple for loop with range
for i in range(5):              # Iterates from 0 up to (but not including) 5
    print(i)                    # Prints 0,1,2,3,4

# Summation using a for loop
sum = 0
for i in range(2, 22, 2):       # Iterates from 2 to 20, step 2 (even numbers)
    sum = sum + i               # Adds each even number to sum
print(sum)                      # Prints 110 (2+4+...+20)

# Guessing game (commented out)
secret_number = 3
guess = 0

# while guess != secret_number: # Loop until user guesses correctly
#     guess = int(input('Guess the number (1-5): '))
#     if guess != secret_number:
#         print('Wrong! Try again.')
# print('You got it!')

# While loop example
count = 0
while count < 5:                # Loop runs while count < 5
    print(count)                # Prints 0,1,2,3,4
    count += 1                  # Increments count

# For loop with break
developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer == 'Naomi':    # When 'Naomi' is found, break out of loop
        break
    print(developer)            # Prints 'Jess' only

# For loop with continue
developer_names = ['Jess', 'Naomi', 'Tom']
for developer in developer_names:
    if developer == 'Naomi':    # When 'Naomi' is found, skip this iteration
        continue
    print(developer)            # Prints 'Jess' and 'Tom'

# Nested for loop with vowels check
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']
for word in words:
    for letter in word:         # Loop through each letter in the word
        if letter.lower() in 'aeiou':   # Check if letter is a vowel
            print(f"'{word}' contains the vowel '{letter}'")
            break               # Stop checking further letters once a vowel is found
    else:                       # Runs if no vowel was found in the word
        print(f"'{word}' has no vowels")

# Collecting even numbers into a list
even_numbers = []

for num in range(21):           # Iterates from 0 to 20
    if num % 2 == 0:            # Checks if number is divisible by 2 (even)
        even_numbers.append(num)# Adds even number to the list

print(even_numbers)             # Prints [0,2,4,6,8,10,12,14,16,18,20]
