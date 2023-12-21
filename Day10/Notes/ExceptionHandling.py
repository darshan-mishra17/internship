# Exception Handling

# What are Errors in Programming?
# The problems that stop the execution of the program
# Errors are of two types: Syntax Errors and Runtime Errors:

# 1. Syntax Error: caused due to incorrect syntax which leads to termination of program
# EX:
"""
x = 10
if x>5:
    print("greater")
"""

# 2. Runtime Errors: Errors during the execution  of the program. There factors like division
# by zero , accessing non-existing elements, accesing elements out of index

# What is an Exception?
# An Exception is a specific type of runtime error that occurs when the program encounters
# a situation that it cannot handle.

# Different types of Exceptions in Python:
# 1. TypeError: This exception is raised when an operation is applied to an object of wrong type
# res = 10 + "20"

# 2. KeyError: trying to access any key that is not found in dictionary
"""
my_dict = {"name":"Silicon"}
print(my_dict["age"])
"""

# 3. IndexError: This exception is raised when an index is out of range for a list, tuple, etc
"""
my_list = [1,2,3,4]
         # 0 1 2 3
print(my_list[4])
"""

# 4. ValueError: This exception is raised when  a function is called with invalid argument or values
"""
x = int("1234")
print(x)  # 1234

x = int("abcd")
print(x) # ValueError
"""
# 5. ZeroDivisionError: This exception is raised whan we try  to divide a number by zero
"""
x = 5
y =0
result = x/y
print(result) # ZeroDivisionError: division by zero
"""
# 6. Attribute Error:
# It is an exception that occurs when you try to access an attribute of an objct that doesnot exist.

"""
class Car:
    def __init__(self, price, name):
        self.price = price
        self.name = name
        
obj1  = Car(200, "Ford")
print(obj1.color)
"""
# How to handle these Exceptions(runtime errors) ?
# Try and Except statements : Catching the Exceptions:
# used to catch and handle exceptions in Python.
# Statements that can cause exception are kept inside the try block
# Statements that handle those exceptions are kept in Except block
"""
try:
    print(x)
except:
    print("Error: x is not defined")

sport = "Cricket"
print("I like to play", sport)
"""
# without try block, the program will crash and raise error

# Catching Specific Exceptions:
# We can define multiple except block for handling differentexceptions
"""
try:
    x = 5
    print(x)   
except NameError:
    print("Variable x is not defined")
except ValueError:
    print("ValueError")
except:
    print("Other type of Error")
      
sport = "Cricket"
print("I like to play", sport)
"""

# Try with Else block:
# Executes only when the try block doesnot raise an exception.
"""
try:
    x=5
except:
    print("Error")
else:
    print(x)
"""
"""
def myFun(x, y):     # x = 3, y=3
    try:
        res = ((x+y) / (x-y))   # 6 / 0 = -5
    except ZeroDivisionError:
        print(" Zero Divison Error")
    else:
        print(res)

myFun(2,3) # -5.0 
myFun(3,3) #
"""

# Finally Keyword in Try Except Block:
# It will always get executed whether try block raises error or not:
# In case of error:
"""
try:
    printx(x)
except NameError:
    print("x is not Defined")
finally:
    print("Try and Except Execution is Finished")
"""

# In case of no Error:
"""
try:
    x=5
    print(x)
except NameError:
    print("Variable not defined")
finally:
    print("Try and Except Execution is Finished")
"""

# Another example:
"""
try:
    x = 5//0
    print(x)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("Execution finished")
"""

# Raising exception:
# user can throw/raise exception using raise Keyword

"""
x = -1

if x<0:
    raise Exception("Number is below Zero")
"""

name = "abcd"

if not type(name) is int:
    raise TypeError("Can't convert strings into integer")

# Advantages of Exception handling:
# 1. makes easier to debug
# 2. Prevents program crashing
# 3.  Separates error handling code from the main code, which increases code readability

# Disadvantages:
# 1. Makes program littel slower
# 2. increases the complexity of code













