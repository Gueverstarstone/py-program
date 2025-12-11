# Global scope refers to variables that are declared outside any functions or classes which can be accessed from anywhere in the program. 
# Here, my_first_name can be accessed anywhere, even inside a function it's not defined in:
my_first_name = 'wantam'

def show_name():
    print(my_first_name)
    show_name()
print(my_first_name)

# Modifying a Global Variable Using global
#  if you want to make a locally scoped variable defined inside a function globally accessible, you can use the global keyword:
# If you try to assign a value to x inside a function without global, Python treats it as a new local variable, not the global one.

x = 10  # Global variable

def modify_global():
    global x       # Tell Python we want to modify the global variable
    x = 20         # This changes the global x
    print("Inside function:", x)

modify_global()     # Inside function: 20
print("Outside function:", x)  # Outside function: 20


# global x tells Python: “Use the x from the global scope, not create a new local variable.”

# After calling modify_global(), the global x is changed.