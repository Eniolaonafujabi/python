from acount import Account


def test_that_check_balance_func():
    eniolaAccount = Account()
    balance: float = eniolaAccount.check_balance()
    assert (0,balance)

def test_that_i_can_increase_balance_func():
    eniolaAccount = Account()
    assert (0,eniolaAccount.check_balance())
    eniolaAccount.deposit(1700)
    assert (1700,eniolaAccount.check_balance())

def test_that_you_cant_deposit_negative_amount():
    eniolaAccount = Account()
    assert (0,eniolaAccount.check_balance())
    eniolaAccount.deposit(-1900)
    assert (0,eniolaAccount.check_balance())

def test_that_i_can_withdraw_from_my_balance(self):
    eniolaAccount = Account()
    assert(0, eniolaAccount.check_balance())
    eniolaAccount.deposit(5000)
    assert(5000, eniolaAccount.check_balance())
    eniolaAccount.withdraw(4000)
    assert(1000, eniolaAccount.check_balance())

