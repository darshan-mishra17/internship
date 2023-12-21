txt1=input("Enter the string 1:")
txt2=input("Enter the string 2:")
c=0
for i in txt1:
    for j in txt2:
        if i == j:
            c+=1
print("Output:",c)