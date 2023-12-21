txt=input("enter a string")
t=txt.split(" ")
for x in t:
    if len(x)%2==0:
        print(x)