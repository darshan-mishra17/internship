# Program to count the Number of Lines in Text File:
# Take filename as userinput:
filename = input("Enter file name: ")

numLines = 0
with open(filename, "r") as file:
    for line in file:
        numLines = numLines+1
        
print(numLines) 
        