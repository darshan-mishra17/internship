f=open(input("enter filename:"),"r")
c=0
s=input("enter the word")
for i in f:
    l=i.split()
    for j in l:
        if j==s:
            c+=1
print(c)

            