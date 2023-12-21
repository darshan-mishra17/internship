
n=int(input("enter a number"))

def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
                s+=i

    return (s==n)
   
if perfect(n):
    print("perfect")
else:
    print("not perfect")