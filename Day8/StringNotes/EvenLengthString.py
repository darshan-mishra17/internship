# Program to print the even length words in a string
"""
input:   1   4   2  3
myStr = "I live in bdk"
Output: live in
"""

myStr = input("Enter the string: ")

list = myStr.split(" ")
newStr=""
for i in list:
    if len(i)%2==0:
        newStr= newStr+" "+i
print(newStr)
        