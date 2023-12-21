# Program to Remove the nth index Character from a Non-Empty String.
# Take User Input
"""      0123456
myStr = "Silicon Institute"
n = 3
"""

def removeIndex(myString,n):
    str1 = myString[:n]
    str2 = myString[n+1:]
    return str1+str2

myStr = input("Enter String: ")

n = int(input("Enter the value of n: "))

print(removeIndex(myStr,n))

