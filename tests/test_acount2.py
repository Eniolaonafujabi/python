import unittest
from acount import Account

class MyTestCase(unittest.TestCase):
    def test_that_i_can_check_balance(self):
        eniolaAccount = Account()
        balance: float = eniolaAccount.check_balance()
        self.assertEqual(0, balance)

    def test_that_i_can_increase_balance(self):
        eniolaAccount = Account()
        self.assertEqual(0,eniolaAccount.check_balance())
        eniolaAccount.deposit(1700)
        self.assertEqual(1700,eniolaAccount.check_balance())

    def test_that_i_can_not_deposit_negative_amount(self):
        eniolaAccount = Account()
        self.assertEqual(0,eniolaAccount.check_balance())
        eniolaAccount.deposit(-1700)
        self.assertEqual(0,eniolaAccount.check_balance())

    def test_that_i_can_withdraw_from_my_balance(self):
        eniolaAccount = Account()
        self.assertEqual(0,eniolaAccount.check_balance())
        eniolaAccount.deposit(5000)
        self.assertEqual(5000,eniolaAccount.check_balance())
        eniolaAccount.withdraw(4000)
        self.assertEqual(1000,eniolaAccount.check_balance())

    def test_that_you_can_not_withdraw_more_than_your_amount(self):
        eniolaAccount = Account()
        self.assertEqual(0,eniolaAccount.check_balance())
        eniolaAccount.deposit(5000)
        self.assertEqual(5000,eniolaAccount.check_balance())
        eniolaAccount.withdraw(6000)
        self.assertEqual(5000,eniolaAccount.check_balance())

    def test_that_you_can_not_withdraw_negative_amount_from_balance(self):
        janetAccount = Account()
        self.assertEqual(0,janetAccount.check_balance())
        janetAccount.deposit(50000)
        self.assertEqual(50000,janetAccount.check_balance())
        janetAccount.withdraw(-10000)
        self.assertEqual(50000,janetAccount.check_balance())
