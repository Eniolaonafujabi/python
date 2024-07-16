class Account:
    def __init__(self, name, pin, accountNumber):
        self.name = name
        self.pin = pin
        self.accountNumber = accountNumber
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount

    def withdraw(self, amount):
        pass

    def check_balance(self, pin):
        if self.check_pin(pin):
            return self.balance
        return 0

    def check_pin(self, pin):
        if self.pin == pin:
            return True
        return False