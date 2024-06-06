from user import User

class CurrentAccount(User):
    def __init__(self):
        User.__init__(self)

current = CurrentAccount()
# amount = int(input("withdraw: "))
current.withdraw()
current.deposit()
