class bankAccounts:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance-amount
        else:
            print("Insufficient Funds")
    def display(self):
        print('the balance:',self.balance)

account_number = int(input("Enter the account number: ")) 
balance = int(input("Enter the current balance: "))
acc1=bankAccounts(account_number,balance)
ch=0
while ch!=4:
    print('\tMENU\t')
    print('1:deposit')
    print('2:withdraw')
    print('3:check balance')
    print('4:exit')
    ch=int(input('enter ur choice: '))
    if ch == 1:
        amt=int(input('enter ur amount to be deposited'))
        acc1.deposit(amt)
    elif ch == 2:
        amt=int(input('enter ur amount to be withdrawed'))
        acc1.withdraw(amt)
    elif ch == 3:
        acc1.display()
    else:
        print("invalid choice")
    
        
    