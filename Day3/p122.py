n=int(input("enter a number"))
for i in range(n+1):
    for j in range(n,i,-1):
        print("*",end=" ")
    print(" ")