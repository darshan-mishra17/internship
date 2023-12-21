list1=[12, 15, 3, 10]
list2=[]
for i in range(len(list1)):
    if i%2!=0:
        list2.append(list1[i])
print(list2)
    

list2 = [11, 5, 17, 18, 23, 50]
del list2[1:5]
print(list2)