from user import User

class StudentAccount(User):
    def __init__(self):
        User.__init__(self)

    def withdraw(self, amount):
        if amount < 2000:
            super().withdraw(amount)
        else:
            print("Amount exceeds limit")

    def deposit(self, amount):
        if amount < 50000:
            super().deposit(amount)
        else:
            print("Amount exceeds limit")

student = StudentAccount()
student.deposit(1000)
student.withdraw(1000)