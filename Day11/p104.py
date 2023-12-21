n=int(input("create no. of employee:"))

class Employee:
    count=0
    def __init__(self):
        Employee.count+=1

for i in range(n):
    obj=Employee()
print(Employee.count)