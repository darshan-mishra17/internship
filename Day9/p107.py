f=open(input("enter filename:"),"r")
l=[]
for i in f:
    for j in i:
        for k in j:
            if k.isdigit():
                l.append(k)
s=set((l))
s=sorted(s)
print(s)