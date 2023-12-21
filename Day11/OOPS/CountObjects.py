# Program to count the number of objects in a class:
"""
class Employee:

    def __init__(self):
        
obj = Employee()
obj = Employee()

n = 10
till n
10 times object created
"""
class Employee:
    count=0
    def __init__(self):
        Employee.count+=1

num = int(input("Enter the number: ")) # 10

for i in range(num):   0 to 9 : 10 times
    obj = Employee()
    
print("Number of objects: ",Employee.count)



