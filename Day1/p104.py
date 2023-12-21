x=input("enter a side one")
x=int(x)
y=int(input("enter a side two"))
z=int(input("enter a side three"))
s=(x+y+z)/2
area=(s*(s-x)+s*(s-y)+s*(s-z))**(1/2)
print("area of the triangle is ",area)