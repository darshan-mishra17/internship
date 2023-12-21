def sortt(x):
    return x[1]
list=[('java',3),('css',0),('c',1),('js',4)]
l=sorted(list,key=sortt)
print(l)