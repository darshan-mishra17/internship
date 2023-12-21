"""
Define a class rectangle with attributes length and breadth. Implement a method called
calculate_area that returns the area of the rectangle.

create an object and set its dimensions and then print the area

Take length and breadth as user input:
"""
class Rectangle:
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def calculateArea(self):
        return self.length * self.breadth
    
length = int(input("Enter the length: "))  # 20 
breadth = int(input("Enter the breadth: ")) # 30

obj = Rectangle(length, breadth)
print("Area is :",obj.calculateArea())
  
  
  
  
  