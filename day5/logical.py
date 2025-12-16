# logical operators - are special operators that allow you to combine multiple expressions to create more complex decision-making logic in your code.
is_citizen = True
age = 25

print(is_citizen and age) # 25

# It doesn’t matter whether the second operand is truthy or falsy — if the first one is truthy, Python always hands back the second value.


# or operator - operator returns the first operand if it is truthy, otherwise, it returns the second operand
is_user = False
name = 'munga'
print(is_user or name)

# using or in one or more expressions
age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

# In this case, age < 18 is False, but is_student is True. Since at least one condition is true, the entire or expression evaluates to True, and the discount message in the if block is printed.

# using the not operator- akes a single operand and inverts its boolean value. It converts truthy values to False and falsy values to True

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')

# Since is_admin is False, then not is_admin is saying not False which is True. So the message Access denied for non-administrators. will be printed.

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("You can watch the movie.")
else:
    print("You can't watch the movie.")