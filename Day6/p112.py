tuple1=(4,5)
tuple2=(6,7)
l=[]
for i in tuple1:
    for j in tuple2:
        l.append(tuple((i,j)))
for i in tuple2:
    for j in tuple1:
        l.append(tuple((i,j)))
        
print(l)