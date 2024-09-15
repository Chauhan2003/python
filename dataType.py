a = 5
print(type(a)) # int

b = "Hello"
print(type(b)) # str

c = 18.75
print(type(c)) # float

d = [1, 2, 3, 4]
print(type(d)) # list

e = (1, 2, 3, 4)
print(type(e)) # tuple

f = {"first": 1, "second": 2, "third": 3}
print(type(f)) # dict

g = True
print(type(g)) # bool


"""
<------------------- Python Numbers --------------------->
There are three numberic type in python:
1. int
2. float
3. complex
"""

x = 1
y = 2.8
z = 5j

print(type(x)) # int
print(type(y)) # float
print(type(z)) # complex

# Type Conversion:

a = float(x)
b = complex(y)
c = complex(x)

print(a) # 1.0
print(b) # (2.8 + 0j)
print(c) # (1 + 0j)


"""
<------------------- Random Number --------------------->
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
"""

import random

print(random.randrange(1, 10)) # between 1 and 9