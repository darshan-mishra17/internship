n=int(input("enter the number of items"))
list=[]
l=[]
for i in range(n):
    list.append(input("enter a word"))
item=(input("enter a word to delete"))
c=0
for x in list:
    if x==item:
        c+=1
if c>1:
    oc=int(input("enter number of occurence"))
    i=0
    for x in list:
        if x==item:
            i+=1
            if i==oc:
                continue
            else:
                l.append(x)
        else:
            l.append(x)
    print(l)
elif c==1:
    list.remove(item)
    print(list)
else:
    print("word does not exist")
    