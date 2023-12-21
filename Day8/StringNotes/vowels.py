# Program to calculate the number of vowels in a string:

myStr = input("Enter the String: ")
count=0
vowels = "aeiou"

for i in myStr.lower():
    if i in vowels:
        count=count+1
        
print(count)