# Problem to find the Area and permimeter of circle using classes:
"""
Area and perimeter should be calculated in two different methods(functions)
"""
import math
class Circle:
    def __init__(self, radius): 
        self.radius = int(input("Enter the Radius: "))
        
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return 2*math.pi*self.radius

radius = int(input("Enter the Radius: "))
obj = Circle(self.radius) 
print("Area : ", round(obj.area(),3))
print("Perimeter: ",round(obj.perimeter(),3))