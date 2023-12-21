l=int(input("enter a lower limit"))
u=int(input("enter a upper limit"))

def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
                s+=i
    return (s==n)


for j in range(l,u+1):
    if perfect(j):
        print(j)