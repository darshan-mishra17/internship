l=[]
n=int(input("enter the size of list"))
for i in range(n):
    l.append(input("enter the character:"))
k=int(input("enter the value of k: "))
l.sort(reverse=True)
fl=l[:k]
print("Input:",l)
print("Output:",fl)
