names = ['wantam', 'mungai', 'zuri', ['dedan', 'nyawi']]

for i in names:
    print(i)

# Print first 10 numbers using a for loop
for num in range(1,10):
    print(num)

# Print sum of all even numbers from 2 to 20
sum = 0
for i in range(2,22,2):
    sum = sum + i
    print(sum)



results = []                           # Start with an empty list

for num in list(range(1,51)):          # Loop through numbers 1 to 50
    if num % 3 == 0 and num % 5 == 0:  # Divisible by both 3 and 5
       results.append('FizzBuzz')      # Add "FizzBuzz" to the list
    elif num % 3 == 0:                 # Divisible by 3 only
        results.append('Fizz')         # Add "Fizz"
    elif num % 5 == 0:                 # Divisible by 5 only
        results.append('Buzz')         # Add "Buzz"
    else:                              # Otherwise
        results.append(num)            # Add the number itself

print(results)                         # Print the entire list at once
print(results.count('Buzz'))

results = [ "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in range(1,51) ]
print(results)

# calculate the square of each number present in the list.
numbers = []
for i in range(2,10):
    square = i ** 2
    numbers.append(square)
    print(f'The square of {i} is: {square}')
    print(numbers)

# Calculate the average of list of numbers
num1 = [10,20,30,40,50]
sum = 0
for i in num1:
    sum = sum+ i
list_size = len(num1)
average = sum/list_size
print(average)

students_marks = [20,30,40,50,60,70]
for marks in students_marks:
    if marks >= 30:
        print(f'{marks}: passed')
    else:
        print(f'{marks}: failed')


# Print all even and odd numbers
result = []
for numbers in range(1,11):
    if numbers % 2 == 0:
        result.append(f'{numbers} is even')
    else:
        result.append(f'{numbers} is odd')

print(result)

# Use for loop to generate a list of numbers from 9 to 50 divisible by 2.
result = []
for numbers in range(9,25):
    if numbers % 2 == 0:
        result.append(f'{numbers} is divisible by 2')
    else:
        result.append(f'{numbers} is not divisible by 2')
print(result)
