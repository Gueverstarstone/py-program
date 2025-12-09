my_str = 'Hello Mungai, "the girl said"'
print('Hello' in my_str)

#Escape the single or double quotation mark in the string with a backslash (\)
my_message = 'Hello Mungai, "the girl said, it\'s raining"'
print(my_message)

#string concatenation using str() function
name = 'Gueverstarstone'
age = 26
print(name + str(age))


# augmented assignment operator for concatenation. 
# This is represented by a plus and equals sign (+=), and performs both concatenation and assignment in one step. Here's it in action:
make = 'subaru'
year = 2006

make_and_year = make
make_and_year += str(year)
print(make_and_year)

#f-strings
# It allows you to handle interpolation and also do some concatenation with a compact and readable syntax.
school = 'jeremy high'
year = 2007
name = 'zuri'

# getting the length of a string using the len() function
print(len(school))

name_and_year = f'my namae is {name} and i was born in {year}'
print(name_and_year)
print(len(name))

my_num = 2
my_number = 3
my_num_and_my_number = f'the sum of {my_num} and {my_number} is {my_num + my_number}'
print(my_num_and_my_number)

# indexing- accessing a character by its index using bracket notation
my_name = 'zuri muthoni'
print(my_name[3])
print(my_name[7])
print(my_name[-1]) #getting the last character with -1

# slicing-String slicing lets you extract a portion of a string or work with only a specific part of it
last_name = 'peter'
print(last_name[1:4]) # 1  is the strt index, 4 is the stop index
# stop index is non-inclusive


# step-used to specify the increment between each index in the slice.
# Here's the syntax for that:
# string[start:stop:step]
# In the example below, the slicing starts at index 0, stops before 11, and extracts every second character:

my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

# A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, and leaving start and stop blank:

my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH

# It can also be helpful to check if a character or set of characters exist in a string before slicing it. 
# To do that, Python provides the in operator, which returns a boolean that specifies whether the character or characters exist in the string or not.

my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

