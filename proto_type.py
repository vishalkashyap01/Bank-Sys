#bank system prototype
class bank:
    bank_name = "SBI"
    account_no = 4128
    balance = 1000
    
    #constructor
    def __init__(self, name):
        self.name = name
        print("Welcome,", name)
        
    #automate withdraw & deposit
    def automate(self):
        print("type 'add' to credit amount")
        print("type 'get' for debit amount")
        print("type 'check' to show bank statement")
        print("type 'close' to kill the app")
        self.command = input("here - ")
        print()
        if self.command == 'add':
            self.money = int(input("amount to credit - "))
            self.credit(self.money)
            self.automate()
            print()
        elif self.command == 'get':
            self.money = int(input("amount to debit - "))
            self.debit(self.money)
            self.automate()
            print()
        elif self.command == 'check':
            self.check_bal()
            self.automate()
            print()
        else:
            self.check_bal()
            print("app is closed...")
            print() 
        
    #credit money
    def credit(self, money):
        self.balance += money
        print(money, "Rupees credited")
        print()
        
    #debit money
    def debit(self, money):
        self.balance -= money
        print(money, "Rupees debitted")
        print()
        
    #total amount
    def check_bal(self):
        print("Bank - ", self.bank_name)
        print("User :", self.name)
        print("Account no. :", self.account_no)
        print("Total balance :", self.balance, "Rupees")
        print()     
        
#Object        
u1 = bank("Vishal")
print()

#calling automate function to start the app
u1.credit(25000)
u1.automate()