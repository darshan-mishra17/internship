import math
class circle:
    def __init__(self,radius):
        self.radius=r
    def circumference(self):
        return 2*math.pi*self.radius
    def area(self):
        return math.pi*self.radius**2


r=int(input('enter the radius'))
circle1=circle(r)
print('Area:',circle1.area())
print('circumference:',circle1.circumference())

        