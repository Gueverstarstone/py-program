# number pattern
def number_pattern(n):

    if not isinstance(n,int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    numbers = []
    for num in list(range(1, n +1)):
        numbers.append(str(num))
    return ' '.join(numbers)
  
print(number_pattern(9))