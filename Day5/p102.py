n=int(input("enter the number of items"))
list=[]
for i in range(n):
    list.append(int(input("enter a number")))    
even=[]
odd=[]
for x in list:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("ODD: "odd)
print("EVEN:"even)