txt=input("enter a string")
c=0
txt=txt.lower()
for i in txt:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o'or i == 'u':
        c+=1
print("number of vowels is :",c)