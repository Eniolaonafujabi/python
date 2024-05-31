from acount import Account


def test_that_check_balance_func():
    eniolaAccount = Account()
    balance: float = eniolaAccount.check_balance()
    assert (0, balance)


def test_that_i_can_increase_balance_func():
    eniolaAccount = Account()
    assert (0, eniolaAccount.check_balance())
    eniolaAccount.deposit(1700)
    assert (1700, eniolaAccount.check_balance())


def test_that_you_cant_deposit_negative_amount():
    eniolaAccount = Account()
    assert (0, eniolaAccount.check_balance())
    eniolaAccount.deposit(-1900)
    assert (0, eniolaAccount.check_balance())


def test_that_i_can_withdraw_from_my_balance():
    eniolaAccount = Account()
    assert (0, eniolaAccount.check_balance())
    eniolaAccount.deposit(5000)
    assert (5000, eniolaAccount.check_balance())
    eniolaAccount.withdraw(4000)
    assert (1000, eniolaAccount.check_balance())

def test_that_i_can_not_withdraw_more_than_my_balance():
    eniolaAccount = Account()
    assert (0, eniolaAccount.check_balance())
    eniolaAccount.deposit(5000)
    assert (5000, eniolaAccount.check_balance())
    eniolaAccount.withdraw(6000)
    assert (5000, eniolaAccount.check_balance())

def test_that_you_can_not_withdraw_negative_amount_from_balance():
    janetAccount = Account()
    assert (0, janetAccount.check_balance())
    janetAccount.deposit(50000)
    assert (50000, janetAccount.check_balance())
    janetAccount.withdraw(-10000)
    assert (40000, janetAccount.check_balance())
