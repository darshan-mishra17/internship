"""
Create a class BankAccount with attributes : account_number and balance
Implement two methods for depositing and withdrawing money and also update the balance

create an object with some transactions and print the before and after balance in the account.

Take user input:

current balance:
withdraw amount: 
deposit amount:


Account number = 12345
balance = 1000

account.withdraw(200)  # 800
account.deposit(300)   # 800+300

balance = 1100
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance+amount
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance-amount
        else:
            print("Insufficient Funds")
    
account_number = int(input("Enter the account number: ")) 
balance = int(input("Enter the current balance: ")) # 5000
withdraw = int(input("Enter the withdraw amount: ")) # 500 = #4500
deposit = int(input("Enter the deposit amount: ")) # 600:  4500+600 = 5100
  
obj = BankAccount(account_number, balance)
obj.withdraw(withdraw)
obj.deposit(deposit)
print("Final balance:",obj.balance)
 
    
    

