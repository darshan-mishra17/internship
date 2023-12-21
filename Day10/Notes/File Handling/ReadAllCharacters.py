# Program to read character by character from a file:
# My name is Ravi
# do it using single loop
"""
M
y

n
a
m
e

i
s

R
a
v
i
"""
filename = input("Enter the filename: ")

file = open(filename,"r")
content = file.read()

for i in content:
    print(i)