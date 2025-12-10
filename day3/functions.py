# functions
# input()
#name = input('what is you name')# User types "Kolade" and presses Enter  
#print(f'hello, {name}')# Output: Hello Kolade

# function using def
def greeting():
    print('my name is gueverstarstone')

greeting()

def calculate_sum(a,b): # passed parameters
    print(a + b)

calculate_sum(8,9) #passing the arguments

# use of return
def addition(a,b):
    return a+ b

my_new_num = addition(1,1)
print(my_new_num)
    