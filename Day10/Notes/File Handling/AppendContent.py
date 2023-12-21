# Program to Append the content of one File to The End of Another File:

"""
# read(), readline(), readlines()

1. read() : reads the entire content of the file a single string.

2. readline() : reads a single line from the file a string. It moves the file pointer to the next line
after reading.

3. readlines() : reads all lines from the file and returns them as a list of strings.
"""

filename1 = input("Enter file to read: ")
filename2 = input("Enter file to append: ")

file = open(filename1, "r")
lines = file.read()
file.close()

file2 = open(filename2, "a+")
file2.write("\n")
file2.write(lines)
print(file2.read())
file2.close()



