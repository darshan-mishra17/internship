n=int(input("enter a number"))
s=0
for i in range(1,n+1):
    if n%i==0:
        s+=1
if(s==2):
    print("prime number")
else:
    print("not prime number")