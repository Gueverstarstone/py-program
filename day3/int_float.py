# integer
# working with addition
my_int = 20
my_int2 = 40
sum_is = my_int + my_int2
print(f'sum of {my_int} + {my_int2} is {sum_is}')
print(type(sum_is))

my_int3 = 56
my_int4 = 12.8
modulo_is = my_int3 % my_int4
print(f'modulo of {my_int3} % {my_int4} is {modulo_is}')
print(type(modulo_is))

my_int5 = 56
my_int6= 12.8
expon_is = my_int5 ** my_int6
print(f'modulo of {my_int5} ** {my_int6} is {expon_is}')
print(type(expon_is))


# float() function to convert an integer into a float by adding a decimal point of 0 to the integer:
my_int7 = 89
my_float = float(my_int7)
print(my_float)
print(type(my_float))

# int() function to convert a float into an integer, which removes the decimal point and everything after it from the float you pass it:
my_float2 = 5.0983727
my_int8= int(my_float2)
print(my_float2)
print(type(my_int8))

#Also, you can use the same built-in functions to convert a string into either a float or integer:
my_str_int = '45'
my_str_float = '7.8'

convert_int = int(my_str_int)
conver_float = float(my_str_float)
print(convert_int)
print(conver_float)

# pow(): raises a number to the power of another or performs modular exponentiation.
result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3