# Two modes in a writing a file:
# 1. "a" : append at the end of file
# 2. "w" : ovverwrite the entire file:
"""
# write() 
file = open("Ravi.txt","a")
file.write("\nWe are learning Python")
file.close()

# open and reading after apending
file = open("Ravi.txt","r")
print(file.read())
"""
# "w" : Overwrites the entire file

file = open("Ravi.txt","w")
file.write("Silicon Institute")

file = open("Ravi.txt","r")
print(file.read())
file.close()


