# local scope-means that a variable declared inside a function or class can only be accessed within that function or class.
def my_name():
    my_var = 'wantam' # Locally scoped to my_var
    print(my_var)
my_name()

# Enclosing scope means that a function that's nested inside another function can access the variables of the function it's nested within.
def inner_func():
    my_name = 'zuriel'

    def inner_func2():
        print(my_name)

    inner_func2()
        
inner_func()