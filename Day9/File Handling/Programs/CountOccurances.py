# Program to count the occurance of a word in a Text file
# take filename and word as input:

filename = input("Enter file name: ")
searchWord = input("Enter word: ")
count=0

with open(filename, "r") as file:
    for line in file:
        words = line.split()
        for i in words:
            if i==searchWord:
                count=count+1
print(count)
