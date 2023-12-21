# PYTHON STRINGS:
# both are same
print("Silicon") # Double Quotes
print('Silicon') # single Quotes

# Multiline strings using triple Quotes
x = """ My name is Ravi,
        I am from bhubaneswar, Odisha.
"""
print(x)

# Three single quotes
x = ''' My name is Ravi,
I am from bhubaneswar, Odisha.
'''
print(x)


# Strings are Array of characters:
# In python , there is no character data type
# so A single Character is a string of length 1
y = "s"
print(y)

# String length:
# using len() function
x = "Silicon"
print(len(x)) # 7

# Access individual characters in a string ??
x  =  "Silicon"
print(x[1])

for i in x:
    print(i)

print("-------------")

for i in range(len(x)):
    print(x[i])
    

# Check whether a string is present inside another string ???
# using in keyword:
msg = "My name is Ravi, I am from bhubaneswar, Odisha."

if "name" in msg:
    print("Present")
else:
    print("Absent")

print("name" in msg)

print("-------------")
# Using not in :

msg = "My name is Ravi, I am from bhubaneswar, Odisha."

if "name" not in msg:
    print("Not Present")
else:
    print("Present")

print("name" not in msg)

# String Slicing:
# used to return a range of characters
# starting index: included
# Ending index: Not included

        #0123456
myStr = "Silicon"
print(myStr[2:5]) # lic
print(myStr[0:0], end="") # Empty String
print(myStr[0:1]) # S

# Strting index not mentioned
print(myStr[:7]) # Silicon
print(myStr[:0]) # Empty String
print(myStr[:1]) # S

# Ending index not mentioned
    #0123456
x = "Silicon"
print(x[0:]) # Silicon


# Negative Indexing:
    #0123456
x = "Silicon"
   #-7654321

print(x[-1:]) # n
print(x[-1:-1]) # Empty String

print(x[-7:-3]) # Sili
print(x[-1:-5]) # Empty String
print(x[-1:-5:-1]) # noci
print(x[-1:-8:-2]) # nclS

# Built-in Strings methods for string manipulation:
# All methods return a new string.

# 1 . upper() : returns a new string in uppercase. Doesnot modify the original one

x = "Silicon"
res = x.upper()
print(res) # SILICON
print(type(res)) # <class 'str'>
print(x) # Silicon
print(x.upper()) # SILICON

# 2 . lower() : returns a new string in lowercase

x = "Silicon"
res = x.lower() # silicon
print(res)

# 3 . strip() : returns a new string after removing space from starting and ending.
x = "  Silicon  "
print(x)
print(len(x))
print("After removing space: ")
print(x.strip())
print(len(x.strip()))

x = "  Silicon  Institute  "
print(x.strip())


# 4 . replace() : replaces a string with another string:
x = "Silicon"
res = x.replace("i","e")
print(res)

x = "Silicon Institute"
res = x.replace("Institute", "college")
print(res)

# 5 . split() : returns a list where the text between the specified separator , becomes list
# items
x = "Silicon, Institute, College"
res = x.split(",")
print(res)

x = "Silicon @ Institute"
res = x.split("@")
print(res)

x = "Silicon : Institute"
res = x.split(",")
print(res)

# Concatenation
x = "Silicon"
y = "Institute"
new = x+" "+y
print(new)

# String formatting:
# process of printing a string as per user's desire

"""
age = 23
msg = "My age is " + age
print(msg) # Error
"""

# 6 . format() method:
# used to format parts of string
# takes many agruments that are placed in the respective placeholder {}
age = 23
msg = "My age is {}"
print(msg.format(age))
print(msg)

# Another example: Multiple values
name = "Ravi"
age = 23
year = 2023
msg = "My name is {}. I am {} years old. I graduated in {}"
print(msg.format(name,age,year))
#output : My name is Ravi. I am 23 years old. I graduated in 2023

# Index numbers can be used for correct placing of values
name = "Ravi"
age = 23
year = 2023
msg = "My name is {2}. I am {0} years old. I graduated in {1}"
print(msg.format(age,year,name))

# Float value:
price = 97.2342
msg = "The price of medicine is {:.2f}"
print(msg.format(price))

price = 97.2342
product = "Medicine"
msg = "The price of {1} is {0:.2f}"
print(msg.format(price, product))
            
#output: The price of Medicine is 97.23"

# Named indexes:
# names can be added inside placeholders
# need to pass the names in parameter values

msg = "The capital of {city} is {state}"
print(msg.format(state="Odisha",city="Bhubaneswar"))


# 7. capitalize(): converts the first character to upper case and the rest is lowercase

msg = "45 the CAPITAL of Bhubaneswar is ODISHA"
newMsg = msg.capitalize()
print(newMsg)

# 8 . casefold() : converts all characters of a string to lowercase

msg = "The CAPITAL of Bhubaneswar is ODISHA"
newMsg = msg.casefold()
print(newMsg)

# 9 . center() : returns a centered string

x = "Silicon"
newStr = x.center(20, "*")
print(newStr)  # ******Silicon*******
print(len(newStr)) # 20

# 10. count() : returns the number of occurances of a specified string in a given string
msg = "The live in Bbsr. I love Bbsr"
x = msg.count("Bbsr")
print(x) # 2

x = msg.count("Bbsr",7)
print(x)  # 1

x = msg.count("Bbsr",4,18)
print(x) # 1

# 11. endswith() : returns True if the given string ends with the  specified value.
                       #17
msg = "The live in Bbsr. I love Bbsr"
x = msg.endswith("Bbsr")
print(x) # True

x = msg.endswith("Bbsr.",2,17)
print(x)

# 12. find() : returns the first occurance of the spcified string
# returns -1 if not present

msg = "The live in Bbsr. I love Bbsr"
x = msg.find("Bbsr")
print(x)  # 12

x = msg.find("City")
print(x)  # -1

# 13. index(): same as find() but if value not found, it will give error
msg = "The live in Bbsr. I love Bbsr"
# x = msg.index("city")
# print(x)  # Error

# 14. isdigit() : returns true when every character is a digit
myStr = "1234"
x = myStr.isdigit()
print(x)

# 15. islower() : returns true if all characters are in lowercase
myStr = "city"
print(myStr.islower()) # True

myStr = "cITy"
print(myStr.islower()) # False

# 16. isupper(): 

# 17. startswith()
msg = "The live in Bbsr. I love Bbsr"
x = msg.startswith("Bbsr",12)
print(x) # True

# 18. join(): it joins all items of an iterable (tuples, list, etc) into string with
# specified character

city = ("Bbsr", "Mumbai","Delhi")

newStr = "*".join(city)

print(newStr)

newStr = " ".join(city)

print(newStr)

subStrings = ("My", "name", "is", "Ravi")
newStr = " ".join(subStrings)
print(newStr)



# 19. swapcase() : converts lowercase characters into upper and vice versa

msg = msg = "The CAPITAL of Bhubaneswar is ODISHA"

x = msg.swapcase()

print(x)
