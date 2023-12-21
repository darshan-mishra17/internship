n=int(input("enter the number of items"))
list=[]
l1=[]
for i in range(n):
    list.append(int(input("enter a number")))
a=int(input("enter the number of items"))
for i in range(a):
    l1.append(int(input("enter a number")))
l=list.copy()
for x in l1:
    l.append(x)
l.sort()
print(l)