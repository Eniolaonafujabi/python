class Account:
    _balance: float = 0.0

    def check_balance(self) -> float:
        return self._balance

    def deposit(self, amount)->None:
        if amount>0 :
            self._balance += amount

    def withdraw(self, amount)->None:
        if amount <= self._balance:
            if amount > 0 :
                 self._balance -= amount



