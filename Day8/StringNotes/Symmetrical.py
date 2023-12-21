# Program to check Whether a String is Symmetrical or Not
"""
myStr = RavRavi
"""

myStr = input("Enter the string: ") # R a v i R a v i
x = len(myStr)//2   x = 4           # 0 1 2 3 4 5 6 7 

str1 = myStr[:x]  # Ravi
str2 = myStr[x:]  # Ravi

if str1==str2:
    print("Symmetrical")
else:
    print("Not Symmetrical")