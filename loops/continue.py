# List of numbers
numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]

# Loop through each number in the list
for i in numbers:
    # If the number is even (divisible by 2), skip this iteration
    if i % 2 == 0:
        continue
    else:
        # Otherwise (odd number), print it
        print(i)

# String to analyze
name = 'Gueverstarstone'

# Counter to keep track of how many times 'e' appears
count = 0

# Loop through each character in the string
for char in name:
    # If the character is not 'e', skip this iteration
    if char != 'e':
        continue
    else:
        # If the character is 'e', increment the counter
        count = count + 1

# Print the total number of times 'e' appeared in the string
print(f'total number of e is: {count}')
