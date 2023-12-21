# With statement:
# Another way of dealing with file handling:

"""
# Without using "with" statement
file = open("Ravi.txt","w")
file.write("Silicon insititute")
file.close()
"""


# using with statement
with open("Ravi.txt", "w") as file:
    file.write("Python Programming")
    
# Automatically closes the file
