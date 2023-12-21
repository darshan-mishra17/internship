class employee:
    def __init__(self,name,company,iD):
        self.name=name
        self.company=company
        self.iD=iD
    def display(self):
        print("NAME:",self.name)
        print("COMPANY:",self.company)
        print("ID:",self.iD)
    
emp1=employee('Darshan','Google',112239)
emp1.display()
        
    