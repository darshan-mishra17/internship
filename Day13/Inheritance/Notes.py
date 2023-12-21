# INHERITANCE:
# capability of one class to derive the properties from another class
# Syntax:
"""
class BaseClass:
    #statement 1....
    .
    .
    .
class childClass(BaseClass):
    #statement 1....
    .
    .
    .
    .
"""
# Composition rather inheritance
# When one class uses another class as a component
"""
class Vehicle:
    
    #class attribute
    name = "Mercedes"
    
class Car(Vehicle):
    def drive(self):
        return "I am driving "+Vehicle.name
    
car = Car()
print(car.drive())
"""
# The car class is not explicitly inherting from vehicle class but it is using the property(name) of vehicle class.

# Now the below code is inherting the property of vehicle class:
"""
# parent class
class Vehicle:
    
    #class attribute
    name = "Mercedes"

# child class
class Car(Vehicle):

    def drive(self):
        return "I am driving "+self.name  
    
car = Car()
print(car.drive())

"""

# The local attribute takes precedence over the inherited atrribute and overrides it.
"""
# parent class
class Vehicle:
    
    #class attribute
    name = "Mercedes"

# child class
class Car(Vehicle):
    name = "BMW"        # local or class attribute
    def drive(self):
        return "I am driving "+self.name  
    
car = Car()
print(car.drive())
"""

# In the below code, Vehicle class has init constructor that takes a name parameter and assigns it to the instance name's attribute
# The Car class inherits from vehicle class, that meaans it inherits the name attribute from parent class
# This way we are using inheritance to share properties and methods between the parent class(Vehicle) and child class(Car)
"""

class Vehicle:
    
    def __init__(self, name):
        self.name = name

class Car(Vehicle):
    
    def drive(self):
        return "I am driving "
    
car = Car("BMW")
print(car.drive())
"""

# Another Example of inheritance
"""
class Parent:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print("My name is "+self.name)
        
class Child(Parent):
    
    def introduce(self):
        print("My name is "+self.name+"  I am Child")

obj = Child("Ravi")
obj.greet()
obj.introduce()
"""
"""
# Error in the below code because parent constructor is not called as child class has its own constructor
# Parent Class
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def displayPerson(self):
        print("Name: ",self.name)
        print("id : ",self.id)

# Child Class
class Employee(Person):
    
    def __init__(self, name , id, salary, profile):
        self.salary = salary
        self.profile = profile

    def displayEmployee(self):
        print("Salary : ",self.salary)
        print("Profile : ", self.profile)

# object of child class:
obj = Employee("Ravi", 1234, 50000, "Developer")
obj.displayPerson()
obj.displayEmployee()
"""

# How to call Parent Constructor from child class

# 1. using parentclassname.__init__
"""
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def displayPerson(self):
        print("Name: ",self.name)
        print("id : ",self.id)

# Child Class
class Employee(Person):
    
    def __init__(self, name , id, salary, profile):
        self.salary = salary
        self.profile = profile
        
        #Person.__init__(self, name, id) # invoking the __init__ of parent using className

    def displayEmployee(self):
        print("Salary : ",self.salary)
        print("Profile : ", self.profile)

# object of child class:
obj = Employee("Ravi", 1234, 50000, "Developer")
obj.displayPerson()
obj.displayEmployee()
"""

#2. Super() Function:
# It is built-in function that returns the object that represents the parent class
# It allows us to access methods  and attributes of parent class from the child class
# We can also call the constructor of parent class from the child class
"""
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def displayPerson(self):
        print("Name: ",self.name)
        print("id : ",self.id)

# Child Class
class Employee(Person):
    
    def __init__(self, name , id, salary, profile):
        self.salary = salary
        self.profile = profile
    
        super().__init__(name, id)      # Super function

    def displayEmployee(self):
        print("Salary : ",self.salary)
        print("Profile : ", self.profile)

# object of child class:
obj = Employee("Ravi", 1234, 50000, "Developer")
obj.displayPerson()
obj.displayEmployee()

"""

# Difference between super().__init__() and parent.__init__():
# Both are used to call the constructor (__init__ method) of parent class but there are some differences

# super().__init__():
# 1. returns a temporary object of the parentclass
# 2. Allows to call methods of parent class without explicitly spcifying the parent class name
# 3. It automatically handles the method resolution order(MRO) in case of multiple inheritance which ensures that
#    right parents class's method is called.
# 4. we don't need to know the name of parent class if the class hierarchy changes

# parent.__init__()
# 1. less fexible in case of multiple inheritance as it doesnot handle the MRO automatically
# 2. This can lead to issues if the class hierarchy changes, since we need to manually update all the refernces to
#    parent classes.

"""
class Parent:
    def __init__(self):
        self.name1 = "Parent Attribute"
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name2 = "child Attribute"
        
obj = Child()
print(obj.name1)
print(obj.name2)
"""



