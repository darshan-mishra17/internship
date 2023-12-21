# Program to Remove the nth index Character from a Non-Empty String.
# Take User Input
"""      0123456
myStr = "Silicon"
n = 3
"""

def removeIndex(myString,n):
    newString = ""
    for i in range(len(myString)):   
        if i != n:                        
            newString = newString + myString[i]  
    return newString

myStr = input("Enter String: ")

n = int(input("Enter the value of n: "))

print(removeIndex(myStr,n))
