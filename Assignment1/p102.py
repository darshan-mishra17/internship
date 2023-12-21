l1 = []
l2 = []
n=int(input("enter the size of list"))
for i in range(n):
    l1.append(input("enter the character:"))
for i in range(n):
    l2.append(int(input("enter the number:")))
print("list 1:",l1)
print("list 2:",l2)
l= list(set(l2))
l.sort()
fl = []
for i in l:
    for j in range(0, len(l2)):
        if(l2[j] == i):
            fl.append(l1[j])
print(fl)