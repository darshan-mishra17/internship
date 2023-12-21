"""
# first Method
file = open("Ravi.txt","r")
print(file.read())
print(" ----------------")
"""
# Second Method
file = open("Ravi.txt","r")
lines = file.readlines()
print(lines)

for line in lines:
    print(line)