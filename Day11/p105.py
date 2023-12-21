class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def CalcArea(self):
        rect.area=self.l*self.b
        return rect.area
        
leng=int(input('enter the length'))
br=int(input('enter the breadth'))
rect1=rect(leng,br)
print("Area is :",rect1.CalcArea())