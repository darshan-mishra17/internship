# Program to check whether a string is palindrome or Not using loop:
"""
myStr1 = "MaddaM"
myStr2 = "MALAYALAM"

OUTPUT:  Palindrome
"""

def checkPalindrome(myStr):
    return myStr==myStr[::-1]

myStr = input("Enter a string: ")
if checkPalindrome(myStr):
    print("Palindrome")
else:
    print("Not Palindrome")


    
