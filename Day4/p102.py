colours=['red','blue','green','yellow','orange']
item=input("enter the element to search")
item=item.lower()
"""for i in range(len(colours)):
    if(colours[i]==item):
        print("found")
        break
else:
    print("not found")
"""
print(item in colours)