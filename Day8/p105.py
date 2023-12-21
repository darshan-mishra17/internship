txt=input("enter a string")
c=0
for i in txt:
    if i.isdigit():
        c+=1
print("the number of digits is:",c)