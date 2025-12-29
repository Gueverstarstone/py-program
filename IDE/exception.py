# Python provides the try, except, else, and finally blocks to gracefully handle errors. Here's a basic example:

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
# try: The block of code where you anticipate an error might occur.

# except: This block runs if an error of the specified type is raised inside the try.

# In this case, dividing by zero raises a ZeroDivisionError, which is then caught and handled.

# And here's an example also showing how to use the else and finally blocks:

try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('Division successful:', x)
finally:
    print('This block always runs.')
# else: Runs if no exception is raised in the try block.

# finally: Runs no matter what—whether or not an exception occurred. Useful for clean-up tasks like closing files or releasing resources.

# You can also catch multiple exceptions with separate except blocks:

try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")
# By using separate except clauses, you can make your error responses more specific and useful.

try:
    # Ask the user to enter the numerator and convert it to a float
    num = float(input('enter numerator: '))
    
    # Ask the user to enter the denominator and convert it to a float
    num2 = float(input('enter denominator: '))
    
    # Perform division
    quotient = num / num2
    
    # Print the result using an f-string
    print(f'Quotient is: {quotient}')

# Handle the case where the user enters something that cannot be converted to a float
except ValueError:
    print('invalid input. please enter a number')

# Handle the case where the denominator is zero (division by zero error)
except ZeroDivisionError:
    print('Invalid input please enter a non-zero denominator')

# The finally block always runs, whether an error occurred or not
finally:
    print('program finished. Cleaning up')
