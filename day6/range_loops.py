# Loop from 0 up to (but not including) 7
for num in range(7):
    print(num)                  # Prints 0,1,2,3,4,5,6

# Loop from 9 up to (but not including) 12
for num2 in range(9,12):
    print(num2)                 # Prints 9,10,11

# Loop from 2 to 10 with step 2 (even numbers)
for num in range(2, 11, 2):
    print(num)                  # Prints 2,4,6,8,10

# Loop backwards from 40 down to (but not including) 0, step -10
for num in range(40, 0, -10):
    print(num)                  # Prints 40,30,20,10

# Create a list directly from range(2,11,2)
numbers = list(range(2, 11, 2))
print(numbers)                  # Prints [2,4,6,8,10]

# 👉 This snippet demonstrates different ways to use range():

# range(start, stop) → counts from start up to stop-1.

# range(start, stop, step) → counts with a custom step (positive or negative).

# Wrapping range() with list() converts the sequence into a list.
