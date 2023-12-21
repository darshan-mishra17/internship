u=s=l=0
txt=input("Enter a string: ")

for i in txt:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    elif i == " ":
        s+=1
print("number of lower case characters:",l)
print("number of upper case characters:",u)
print("number of white spaces characters:",s)