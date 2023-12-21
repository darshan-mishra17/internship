tup=[('java',4) , ('python',0) , ('java',2) , ('apple',2)]


def customSort(y):
    
    return y[1]
,y[0]


def secondItem(x):
    
    return sorted(x,key=customSort)
print(secondItem(tup))
#copy from sir