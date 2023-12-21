# Program to calculate number of digits in a string:

myStr = input("Enter String: ")
count = 0
for i in myStr:
    if i.isdigit():
        count=count+1
    
print(count)