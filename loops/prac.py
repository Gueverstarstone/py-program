# List of numbers
numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]

# Loop through the list in reverse order and print each element
for i in reversed(numbers):
    print(i)

print('reverse numbers')

# Example of using range with a negative step
# range(5, -1, -2) → starts at 5, goes down to 0, stepping by -2
for num in range(5, -1, -2):
    print(num)

# -------------------------------
# Nested for loop to print an inverted triangle of stars
rows = 5
for i in reversed(range(1, rows + 1)):   # counts down from 5 → 1
    for j in range(1, i + 1):            # prints stars equal to row number
        print('*', end=' ')
    print('')                            # move to next line

# Nested for loop to print a normal triangle of stars
rows = 5
for i in range(1, rows + 1):             # counts up from 1 → 5
    for j in range(1, i + 1):            # prints stars equal to row number
        print('*', end=' ')
    print('')

# -------------------------------
# Diamond shape (upper + lower triangle)
rows = 5

# Upper triangle
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print('')

# Lower inverted triangle
for i in reversed(range(1, rows)):
    for j in range(1, i + 1):
        print('*', end=' ')
    print('')

# -------------------------------
# While loop inside for loop
# Print multiplication tables for numbers 1 → 5
for i in range(1, 6):                    # outer loop for each table
    print('Multiplication table of:', i)
    count = 1
    while count < 11:                    # inner loop prints products up to ×10
        print(i * count, end=' ')
        count = count + 1
    print('\n')                          # newline after each table

# -------------------------------
# Print each character of a string
name = 'Guevertarstone'
for i in name:
    print(i, end=' ')

# Print each character of the string in reverse order
for i in name[::-1]:
    print(i, end=' ')
