# Enclosing scope means that a function that's nested inside another function can access the variables of the function it's nested within
def my_name():
    my_first_name = 'rigathi'

    def name2():
        print(my_first_name)

    name2()
my_name()



# enclosing scope 2
def outer_func():
    # Variable in outer_func's local scope
    msg = 'Hello there!'
    
    # Variable we want to modify from inner_func
    res = ""  

    # Nested function
    def inner_func():
        # Tell Python we want to modify 'res' from the enclosing scope
        nonlocal res
        
        # Modify the 'res' variable defined in outer_func
        res = 'How are you?'
        
        # Access 'msg' from outer_func (reading is allowed without nonlocal)
        print(msg)

    # Call the inner function
    inner_func()
    
    # Print the modified 'res' after inner_func has run
    print(res)

# Call the outer function
outer_func()
# Output:
# Hello there!
# How are you?
