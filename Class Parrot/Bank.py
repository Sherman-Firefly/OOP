class bank:
    def __init__(self, name, balance=0):
        self.name=name
        self.balance=balance

    def deposit(self, num):
        self.balance += num
        print(num, "Deposited")
        print("New balance", self.balance)

    def withdraw(self, num):
        if num < self.balance:
            self.balance -= num
            print(num, "withdrew")
            print("New balance", self.balance)
        else:
            print("Insufficient amount")
    
    def check(self):
        return self.balance
    
money=bank("Dave", 100)
print(money.deposit(500))
print(money.withdraw(200))
print(money.check())