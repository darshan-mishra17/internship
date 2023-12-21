# Program to copy one File to Another File
# Ravi.txt
# Copy.txt

file = open("Ravi.txt","r")
file2 = open("copy.txt","w")
lines = file.readlines()

for line in lines:
    print(line)
    file2.write(line)

file3 = open("copy.txt")
print(file3.read())