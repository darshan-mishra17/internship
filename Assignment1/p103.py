n=int(input("enter the size of tuple"))
l=[]
for i in range(n):
    l.append(int(input("enter the number:")))
l.sort()
k=int(input("enter the value of k: "))
l1=l[:k]
l2=l[-k:]
fl=l1+l2
mytuple=tuple((l))
print("Input:",mytuple)
finaltuple=tuple((fl))
print("Output:",finaltuple)