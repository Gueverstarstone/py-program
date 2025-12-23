def my_num(x):
    return x ** 2
print(my_num(8))

def my_name(name):
    return 'hello ' + name
print(my_name('Mungai'))

my_name2 = lambda message:message + ' Mungai'
print(my_name2('Welcome home'))

numbers = [1,2,3,4,5,6,7,8,9]
even_numbers = list(filter(lambda num:num % 2 == 0,numbers))
print(even_numbers)

