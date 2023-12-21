txt=input("enter a string")
nwtxt1=''
nwtxt2=''
if len(txt)%2!=0:
    print(assymetrical)
else:
    i=len(txt)//2
    nwtxt1=txt[:i]
    nwtxt2=txt[i:]
    if nwtxt1==nwtxt2:
        print("symmetric")
    else:
        print("assymetric")