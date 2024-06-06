from account import Account
class savingsaccount(Account):
    def __init__(self):
        Account.__init__(self)
        self.interest_rate = 0.05
        self.withdrawal_limit = 700000

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.balance += self.interest_rate
        print('' + str(self.balance))
      

    def withdrawal(self, amount):
        self.balance = self.balance - amount
        if amount <= 700000:
            print('Transaction approved' + str(self.balance))
            
        else:
            print("you can not withdraw above your limit")

y = savingsaccount()
y.deposit(10000000)
y.withdrawal(5000)