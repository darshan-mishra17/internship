l1=[1,2,3,4]
l2=[11,33,55]
l3=l1+l2
print(l3)

l4=l1.copy()
l4.extend(l2)
print(l4)

l5=l1.copy()
for i in l2:
    l5.append(i)
print(l5)

print(l1)
print(l2)