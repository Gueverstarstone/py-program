names = ['mungai','linton','anne']
names[2] = 'munga'
print(len(names))

def addition(a,b):
    return a+ b

print(addition(6,9))

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
