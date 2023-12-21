# Program to count the Number of Blank Spaces in a Text file
# Take filename as userinput:

filename = input("Enter file name: ")
count=0
space=0
with open(filename, "r") as file:
    for line in file:
        words = line.split()
        print(words)
        count = count+len(words)-1
        print(count)
    space = space+count

print(space)