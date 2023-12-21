# "a+" : append and then read.
"""
file = open("Ravi.txt", "a+")
file.write("\n My name is Ravi")
file.seek(0)   # It will read from the starting of the file till end of the file
print(file.read())
file.close()
"""

# file.seek(10) : It will read from the 10th character til the end of file
# "r+" : read and write
"""
file = open("Ravi.txt", "r+")
print(file.read())
print("After Writing: ")
file.write("\n My name is Ravi")  
file.seek(0)
print(file.read())
"""

# In the belwo example, we are directly writing without reading. So the cursor will be at the start of the file
# So it will start replacing the characters from the begining of the file till the end of the sentence that is
# passed through write func
"""
file = open("Ravi.txt", "r+")
file.write("My college Name is Silicon")
print(file.read()) 
"""

# "w+" : write and read data. It will override the existing data.
"""
file = open("Ravi.txt", "w+")
file.write("Ravi")
file.seek(0)
print(file.read())
"""





