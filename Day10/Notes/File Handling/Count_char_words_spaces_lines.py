# Program to count the number of characters, words, spaces and lines in a file:
"""
file = My name is Ravi
characters = 15 #
words = 4
spaces = 3
lines = 1
"""
file = open("Ravi.txt","r")

content = file.readlines()  # returns list of lines

lines = len(content)       

file.seek(0)             # takes cursor to start

content = file.read()

characters = len(content)

words = len(content.split())
spaces = words - lines

print(lines)
print(characters)
print(words)
print(spaces)

