import unittest

from account2 import Account


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.eniola_account = Account('Onafujabi Eniola', '1111', '8146997803')

    def test_account_balance_is_zero(self):
        self.assertEqual(0, self.eniola_account.check_balance('1111'))  # add assertion here8


if __name__ == '__main__':
    unittest.main()
