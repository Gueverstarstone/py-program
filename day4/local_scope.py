# Local scope means that a variable declared inside a function or class can only be accessed within that function or class.
def my_func():
    my_name = 'mungai' # Locally scoped to my_func
    print(len(my_name))
my_func()