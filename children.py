from user import User

class ChildrenAccount(User):
    def __init__(self):
        User.__init__(self)




children = ChildrenAccount()
children.get_interest_rate(1000)
children.withdraw(1000)