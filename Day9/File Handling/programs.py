"""
# creating a new file:
f = open("Ravi.txt","x")

# file located in the same folder where the python code is located
# open() fun returns a file object which contains read() for reading the contents of file

file = open("Ravi.txt")
print(file.read())

# same as:

file = open("Ravi.txt","rt")
print(file.read())

# If is located in different folder
# using double backslashh
file = open("C:\\Users\\ASUS\\Desktop\\RaviDesktop.txt","r")
print(file.read())
"""
# using raw string:
# file = open(r"C:\Users\ASUS\Desktop\RaviDesktop.txt","r")
# print(file.read())

# by default read() method returns the whole text
# we can specify the number of characters

# returns the first 10 characters
"""
file = open("Ravi.txt")
print(file.read())
"""

# reading one line at a time
# using readline() function

"""
file = open("Ravi.txt","r")
print(file.readline())
print(file.readline())
"""

# For reading entire file line by line
f = open("Ravi.txt","r")
for x in f:
    print(x)

