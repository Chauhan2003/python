"""
Python can be used on a server to create web applications.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.

Python run on an interpreter system.
Python latest version is Python 3.
"""

print("Hello Gagan")

"""
<------------------- Python Indentation --------------------->
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
Python uses indentation to indicate a block of code.
"""

if 5 > 2:
    print("Five is greater than two")

"""
<------------------- Python Variables --------------------->
Variables are containers for storing data values.
Python is dynamically typed languages, type checking takes place at runtime or execution time.
Variable names are case-sensitive.
"""

number = 5 # number will be 5
name = "Gagan Chauhan" # name will be 'Gagan Chauhan'

"""
<------------------- Python Casting --------------------->
If you want to specify the data type of a variable, this can be done with casting.
"""

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

"""
<------------------- Get The Type --------------------->
You can get the data type of a variable with the type() function.
"""

print(type(y))
print(type(name))

"""
<------------------- Unpack a Collection --------------------->
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
"""

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""
<------------------- Global Variables --------------------->
Variables that are created outside of a function are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
"""

global_var = 10
def function():
    local_var = 5
    print("Inside function", global_var, local_var)

function()
# print("Outside function", global_var, local_var) -> NameError: name 'local_var' is not defined.
print("Outside function", global_var)

# To create a global variable inside a function, you can use the global keyword.
def function2():
    global var
    var = "Hello"
    print("Inside function", var)

function2()
print("Outside function", var)

# Also, use the global keyword if you want to change a global variable inside a function.

num = 5
def function3():
    global num
    num = 10
    print("Inside function", num)

function3()
print("Outside function", num)