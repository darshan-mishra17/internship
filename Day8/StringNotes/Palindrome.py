# Program to check whether a string is palindrome or Not using loop:
"""
myStr1 = "MaddaM"
myStr2 = "MALAYALAM"

OUTPUT:  Palindrome


myStr = MaddaM
revStr = MaddaM

palindrome
"""

def checkPalindrome(myStr):    # myStr = Python
    revStr=""                  # revStr = ""
    
    for i in myStr:            # i = P,y,t,h,o,n
        revStr = i+revStr      # revStr = nohtyP
                # t + yP
    return newStr==myStr    

myStr = input("Enter a string: ")  # Python

if checkPalindrome(myStr):  #   
    print("Palindrome")
else:
    print("Not Palindrome")


    