# conditionals, let you control the flow of your program based on whether certain conditions are true or false.
# use of if
age = 18
if age >=18:
    print('eligible to drive')

# use of if and else
age2 = 16
if age2 <= 15:
    print('underage')
else:
    print('you can take an ID')


# There might be situations in which you want to account for multiple conditions. To do that, Python lets you extend your if statement with the elif (else if) keyword.
# Note that you can use as many elif statements as you want:
age3 = 2

if age3 >= 65:
    print('You are a senior citizen')
elif age3 >= 30:
    print('You are an adult in your prime')
elif age3 >= 18:
    print('You are a young adult')
elif age3 >= 13:
    print('You are a teenager')
elif age3 >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant