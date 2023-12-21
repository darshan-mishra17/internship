f=open(input("enter filename:"),"r")
c=0
for i in f:
    for j in i:
        if j ==" ":
            c+=1
print(c)