class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b
a=int(input('Enter a number'))
b=int(input('Enter a number'))
obj=Calc(a,b)
ch=0
while ch!=5:
    print('\tMENU\t')
    print('1:ADD')
    print('2:SUBSTRACT')
    print('3:MULTIPLY')
    print('4:DIVIDE')
    print('5:exit')
    ch=int(input('enter ur choice: '))
    if ch == 1:
        print("sum is:",obj.add())
    elif ch == 2:
        print("difference is:",obj.sub())
    elif ch == 3:
        print("product is:",obj.multiply())
    elif ch == 4:
        print("quitent is:",obj.divide())
    else:
        print("invalid choice")
