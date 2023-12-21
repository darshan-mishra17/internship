# Program to find the line number in which the given word is present:
"""
My name is Ravi 
My age is 23
I am teaching Python

take user input = Python
output = Python is present in line 3.
"""
filename = input("Enter file name: ")
word = input("Enter the word: ")
count=0
with open(filename, "r") as f:
    for line in f:
        count+= 1
        if word in line:
            print(word,"is present in line Number",count)
            break
    else:
        print("Word not found")