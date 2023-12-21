class Prime:
    def __init__(self,lb,ub):
        self.lb=lb
        self.ub=ub
    def check(self,i):
        for j in range(2,i):
            if i%j==0:
                return False
            else:
                return True
    def loop(self):
        l=[]
        for i in range(self.lb,self.ub):
            if self.check(i):
                l.append(i)
        return l
            

lb=int(input('Enter a number'))
ub=int(input('Enter a number'))            
obj=Prime(lb,ub)
print('Prime Numbers:\n',obj.loop())
