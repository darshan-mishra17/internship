txt=input("enter a string")
n=int(input("enter the value of n"))
newtxt=''

for i in range(len(txt)):
    if i == n:
        continue
    else:
        newtxt+=txt[i]
print(newtxt)