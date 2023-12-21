# Program to remove Odd indexed Characters in a String:
# Storing the even indexed characters
"""      0123456
myStr = "Silicon" 
"""
def removeOddIndex(myString):
    newString = ""
    for i in range(len(myString)):   
        if i%2 != 0:                        
            continue
        else:
            newString = newString + myString[i]  
    return newString
myStr = input("Enter String: ")
print(removeOddIndex(myStr))

