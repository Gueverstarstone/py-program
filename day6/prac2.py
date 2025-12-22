developer = 'Naomi'
result = developer.endswith('N')
print(result)  
# False → because 'Naomi' does not end with 'N' (it ends with 'i')

my_num = 5
my_num2 = 1.1
result2 = my_num + my_num2
print(result2)  
# 6.1 → adds integer 5 and float 1.1

def addition(a,b):
    return a+b
print(addition(5,6.5))  
# 11.5 → returns the sum of 5 and 6.5

def greet():
    pass
print(greet())  
# None → function has no return, so Python returns None by default

def my_name(a):
    return a.isupper()
print(my_name('mungai'))  
# False → 'mungai' is lowercase, so .isupper() returns False

message = 'python is fun'
print(message[0:6])  
# 'python' → slicing from index 0 up to (but not including) 6
print(message.split())  
# ['python', 'is', 'fun'] → splits the string into words by spaces

table = str.maketrans({'a': '@', 's': '$'}) 
text = "password" 
print(text.translate(table))  
# p@$$word → replaces 'a' with '@' and 's' with '$'

int_1 = 4
int_2 = 2

print(int_1 ** int_2)  
# 16 → exponentiation operator (**). 4 ** 2 means 4 squared = 16
