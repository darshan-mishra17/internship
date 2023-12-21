l=int(input("enter a lower limit"))
u=int(input("enter a upper limit"))

for j in range(l,u):
    c=0
    for i in range(1,j+1):
        if j%i==0:
            c+=1
    if(c==2):
        print(j)