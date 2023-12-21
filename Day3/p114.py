n=int(input("enter a number"))
l=0
for i in range(1,n):
    if n%i==0:
        if l<i and i!=n:
            l=i
print("Largest is :",l)

#best case
for j in range(2,n):
    if n%j==0:
        break
print("largest is :",n//j)