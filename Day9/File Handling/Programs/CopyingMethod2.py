# Program to copy one File to Another File
# Ravi.txt
# Copy.txt

with open("Ravi.txt") as file:
    with open("copy.txt", "w") as file2:
        for line in file:
            file2.write(line)
            
f = open("copy.txt")
print(f.read())
    

