# for loop
names = ['wantam', 'mungai', 'zuri', ['dedan', 'nyawi']]
for name in names: # Take each element from the list names, one by one, and assign it to the variable name.
    print(name)

# use a for loop to iterate through other iterables like a string
for car in 'subaru':
    print(car)

# nesting
foods = ['pilau','meat','waru']
fruits = ['mango','apple','orange']
for food in foods:
    for fruit in fruits:
        print(food,fruit)