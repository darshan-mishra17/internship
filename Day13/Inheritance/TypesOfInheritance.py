# TYPES OF INHERITANCE:
# 1. Single inheritance: One child class inherits from a single parent class
# 2. Multiple Inheritance: One Child class inherits from multiple parent class
# 3. Multilevel Inheritance: One Child class derives from another parent class which in turn derives from another
#    parentclass
# 4. Hierarchical Inheritance: Multiple Child class inherit from a single base class
# 5. Hybrid(or Mixed) Inheritance: Combination of different types of inheritance
#       E.g multiple +  hierarchical


# 2. Mutiple Inheritance:
# When a class is derived from more than one base/Praent class, it is called Multiple inheritance
# The derived class(or child class) inherits all features of the base classes
# Syntax:
"""
class Base1:
    body of the class
    
class Base2:
    body of the class
    
class Derived(Base1, Base2):
    Body of the class
"""
# Example:
"""
# base class 1:
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
    
    def count_wheels(self):
        print("This Vehicle has ", self.wheels, "wheels.")

# base class 2:
class Engine:
    def __init__(self, fuel):
        self.fuel = fuel
        
    def start(self):
        print("Engine started. Fuel type : ", self.fuel)
        
# Derived class:
class Car(Engine, Vehicle):
    def __init__(self, wheels, fuel):
        super().__init__(fuel)
        Vehicle.__init__(self, wheels)
                                 
    def drive(self):
        print("Car is Moving")      
        
my_car = Car(4, "Petrol")
my_car.count_wheels() 
my_car.start()
my_car.drive()
"""

# 3. Multilevel Inheritance:
# one class derives from another class which in turn derives from another class
# Example:
"""
# Base class1
class GrandFather:
    def __init__(self, grandFatherName):
        self.grandFatherName = grandFatherName

# Intermediate Class
class Father(GrandFather):
    def __init__(self, fatherName, grandFatherName):
        self.fatherName = fatherName
        
        super().__init__(grandFatherName)
              
# Derived Class
class Son(Father):
    def __init__(self, sonName, fatherName, grandFatherName):
        self.sonName = sonName
        
        super().__init__(fatherName, grandFatherName)
        
    def printNames(self):
        print("GrandFather : ", self.grandFatherName)
        print("Father : ", self.fatherName)
        print("Son : ", self.sonName)

obj = Son("Prince", "John", "James")
obj.printNames()

"""
# 4. Hierarchical Inheritance:
# Multiple Child class inherit from a single base class
# when more than one derived class are created from a single base class
# Example:
"""
# Base 
class Shape:
    def __init__(self, color):
        self.color = color
       
    def displayColor(self):
        return self.color
    
# Derived class 1   
class Circle(Shape):  
    def __init__(self, circolor):
         super().__init__(circolor)

# Derived class 2
class Rectangle(Shape):
    def __init__(self, recColor):
        super().__init__(recColor)
        
obj1 = Circle("red")
print("Circle color: ", obj1.displayColor())

obj2 = Rectangle("blue")
print("Rectangle Color:", obj2.displayColor())

"""

# 5. Hybrid(or Mixed) Inheritance: Combination of different types of inheritance

class Base1:
    def fun1(self):
        print("Base 1 class")
       
class Parent1(Base1):
    def fun2(self):
        print("Parent 1 class")
            
class Parent2:
    def fun3(self):
        print("Parent 2 class")
    
class child(Parent1, Parent2):
    def fun4(self):
        print("Child class")
    
obj = child()
obj.fun2()
obj.fun3()
obj.fun4()
obj.fun1()

