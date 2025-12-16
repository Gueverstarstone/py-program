is_citizen = True
age = 18

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
        # using bool() function to check whether a value is truthy or falsy
        print(bool('You are eligible to vote'))
else:
    print('You are not eligible to vote')

# The above example will first check if is_citizen is True. 
# If so, it will then go to the nested if statement and check if age is greater than or equal to 18. 
# Since age is greater than or equal to 18, the message printed to the terminal will be You are eligible to vote. 
# If is_citizen were False, then the message printed to the terminal would have been You are not eligible to vote.


# If you are working with more complex conditional statements, then you can use Python’s and, or, and not operators.

# If you want to check whether a value is truthy or falsy, you can use the built-in bool() function.