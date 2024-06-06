from user import User

class Savings(User):
    def __init__(self):
        User.__init__(self)

    def withdraw(self, amount):
        if amount < 700000:
            super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded")

savings = Savings()
savings.withdraw(1000)
savings.get_interest(1000)

