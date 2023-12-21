# Program to Capitalize First Letter of each Word in a File
# title(): returns a string where the first character of every word is in upper case

filename = input("Enter file name: ")

with open(filename, "r") as file:
    lines = file.readlines()
    
print(lines)
newLines=[]

for line in lines:
    newLines.append(line.title())
    
print(newLines)

with open(filename, "w") as file2:
    file2.writelines(newLines)
    
f = open(filename, "r")
print(f.read())