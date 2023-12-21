n=int(input("enter the number of items"))
list=[]
for i in range(n):
    list.append(input("enter a word"))
l=0
for x in list:
    if l<=len(x):
        l=len(x)
        a=x
print("longest is",a ," ",l)