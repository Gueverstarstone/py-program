def name():
    print('my name is mungai')
name()

def my_func(a,b):
    return a + b
addition = my_func(5,5)
print(addition)


def my_num():
    my_var = 'welcome'
    def my_num2():
        print(my_var)

    my_num2()
my_num()

def my_num4():
    my_var2 = 'Hello'
    my_var3 = ''


    def my_num3():
        nonlocal my_var3
        my_var3 = 'How are you?'
        print(my_var2)

    my_num3()
    print(my_var3)
my_num4()