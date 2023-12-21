class Vechile:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def display1(self):
        print("Company:",self.make)
        print("Model:",self.model)
        if self.__class__ == Car:
            print("wheels:",self.wheels)
        else:
            print("fuel type",self.fuelType)
    

class Bike(Vechile):
    def __init__(self,make,model,fuelType):
        self.fuelType=fuelType
        
        super().__init__(make,model)
class Car(Vechile):
    def __init__(self,make,model,wheels):
        self.wheels=wheels
        
        super().__init__(make,model)

make=input("enter the company name:")
model=input("enter the model name:")
wheel=input("enter the wheel name:")

car1=Car(make,model,wheel)
car1.display1()
make1=input("enter the company name:")
model1=input("enter the model name:")
fuelType1=input("enter the fuel type name:")
bike1=Bike(make1,model1,fuelType1)
bike1.display2()