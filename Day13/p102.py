class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Display(self):
        print('Name:',self.name)
        print('age:',self.age)
        print('roll no:',self.rollNo)
        print('Grade:',self.grade)
        print(self.isStudying())
    
class Student(Person):
    def __init__(self,name,age,rollNo,grade):
        self.rollNo=rollNo
        self.grade=grade
        super().__init__(name,age)
    def isStudying(self):
        return True
obj=Student('sam',12,11,'B')
obj.Display()
