no=[28,23,7,5]
"""print(no)
no.sort()
print(no)
no.sort(reverse=True)"""
print(no)
def customSort(no):
    return no%3
    
no.sort(key=customSort)
print(no)