import os


class Account():
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.balance = int(f.read().strip())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
    
    def commit(self, filepath):
        with open(filepath, 'w') as f:
            f.write(str(self.balance))

class CheckingAcount(Account):
    type = ""
    def __init__(self, filepath, fee):
        super().__init__(filepath)
        self.fee = fee

    def transfer(self, amount):
        self.withdraw(amount)
        self.balance -= self.fee


dir = os.path.dirname(__file__)
filepath = os.path.join(dir, 'balance.txt')
account1 = CheckingAcount(filepath, 1)
account1.transfer(500)
account1.deposit(700)
account1.commit(filepath)
