class employee:
    count = 0  

    def __init__(self):
        employee.count += 1  


obj1 = employee()
obj2 = employee()
obj3 = employee()

print("Number of objects created:", employee.count)
