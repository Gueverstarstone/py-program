# Collecting even numbers into a list
even_numbers = []

for num in range(21):           # Iterates from 0 to 20
    if num % 2 == 0:            # Checks if number is divisible by 2 (even)
        even_numbers.append(num)# Adds even number to the list

print(even_numbers)             # Prints [0,2,4,6,8,10,12,14,16,18,20]


# COMPREHENSION
# List comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets.
# The above code can be shortened like this:
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)             # Prints [0,2,4,6,8,10,12,14,16,18,20]


# Conditional comprehension: label numbers as Even or Odd
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)                   # Prints [(1,'Odd'),(2,'Even'),(3,'Odd'),(4,'Even'),(5,'Odd')]


# Using filter() to select words longer than 4 characters
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4        # Condition: word length greater than 4

long_words = list(filter(is_long_word, words))
print(long_words)               # Prints ['mountain','river','cloud']


# Using map() to transform values (Celsius → Fahrenheit)
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32    # Conversion formula

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)               # Prints [32.0,50.0,68.0,86.0,104.0]


# Using sum() to add numbers in a list
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total)                    # Prints 50 (5+10+15+20)


# sum() with optional start argument (positional)
numbers = [5, 10, 15, 20]
total = sum(numbers, 10)        # Adds 10 as starting value → 10+50=60
print(total)                    # Prints 60


# sum() with optional start argument (keyword)
numbers = [5, 10, 15, 20]
total = sum(numbers, start=10)  # Same as above, but using keyword
print(total)                    # Prints 60
