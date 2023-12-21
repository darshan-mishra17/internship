f=open("demo.txt","r")
file=open("copy.txt",'w')
for i in f:
    file.write(i)
file.close()
file=open("copy.txt",'r')
print(file.read())