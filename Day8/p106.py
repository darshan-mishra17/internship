txt=input("enter a string")
c=0
newtxt=''
for i in txt:
    if c%2 == 0:
        newtxt+=i
    c+=1
print(newtxt)
