import math
result = math.floor(609.056984)
print(result)

import math as m
result = m.sqrt(16)
print(result)

from math import pi
print(pi)

from math import floor as f
print(f(9.335735)) 

from math import *
print(sqrt(16))   # 4.0
print(floor(9.8)) # 9
print(pi)         # 3.141592653589793


import datetime
birthday = datetime.date(1959, 7, 15)
print(birthday.day)    # 15
print(birthday.month)  # 7
print(birthday.year)   # 1959


today = datetime.date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)

# file: greetings.py
def say_hello():
    print("Hello!")

if __name__ == "__main__":
    say_hello()


# file: calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    # This part runs only when executed directly
    print(add(2, 3))   # 5

