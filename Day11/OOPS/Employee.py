"""
Define a class named Employee with attributes name, company and id. Initilaize the
attributes uisng the __init__method. Create an object of the class and print the
Employee's details
"""
class Employee:
    #constructor
    def __init__(self,name, company, id):
        self.name = name
        self.company = company
        self.id = id
    
    #method to display
    def display(self):
        print("Name: ",self.name)
        print("Company: ", self.company)
        print("Id: ",self.id)
        
obj = Employee("Ravi","Silicon",11908621)
obj.display()