n=int(input("enter the size of list"))
list=[]
l=[]
for i in range(n):
    list.append(int(input("enter the number")))
for x in list:
    l.append(tuple((x,x**3)))
print(l)
    