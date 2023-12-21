n=int(input("enter the number of items"))
list=[]
for i in range(n):
    list.append(int(input("enter a number")))    
print(sum(list)/n)