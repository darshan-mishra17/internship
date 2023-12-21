n=int(input("enter the number of items"))
list=[]
for i in range(n):
    list.append(int(input("enter a number")))
num=int(input("enter the number to check"))
c=0
for x in list:
    if x==num:
        c+=1
print("Count ",c)