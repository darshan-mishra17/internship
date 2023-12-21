# Program to print each word of a file one by one
"""
Ravi.txt: My name is Ravi

My
name
is
Ravi
"""

filename = input("Enter file name: ")

with open(filename, "r") as file:
    for x in file:
        for word in x.split():
            print(word)