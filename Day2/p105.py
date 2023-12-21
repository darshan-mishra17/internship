s1=int(input("enter the marks of subject 1:"))
s2=int(input("enter the marks of subject 2:"))
s3=int(input("enter the marks of subject 3:"))
s4=int(input("enter the marks of subject 4:"))
s5=int(input("enter the marks of subject 5:"))
avg=(s1+s2+s3+s4+s5)/5
if(avg>=90):
    res="A"
elif(avg<90 and avg>=80):
    res="B"
elif(avg<80 and avg>=70):
    res="C"
else:
    res="D"
    
print("The grade obtained is "+res)
print(type(s1))