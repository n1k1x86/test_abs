import unittest
from atm import ATM


class TestATM(unittest.TestCase):
    def test_deposit(self):
        atm = ATM()
        atm.deposit([1, 2, 3, 4, 5])
        self.assertEqual(atm.banknotesTotal, [1, 2, 3, 4, 5])

    def test_withdraw_success(self):
        atm = ATM()
        atm.deposit([1, 1, 1, 1, 1])
        self.assertEqual(atm.withdraw(850), [0, 1, 1, 1, 1])
        self.assertEqual(atm.banknotesTotal, [1, 0, 0, 0, 0])

    def test_withdraw_partial_success(self):
        atm = ATM()
        atm.deposit([10, 10, 10, 10, 10])
        self.assertEqual(atm.withdraw(370), [2, 1, 1, 1, 0])
        self.assertEqual(atm.banknotesTotal, [8, 9, 9, 9, 10])

    def test_withdraw_failure_not_enough_funds(self):
        atm = ATM()
        atm.deposit([1, 1, 1, 1, 1])
        self.assertEqual(atm.withdraw(2000), [-1])
        self.assertEqual(atm.banknotesTotal, [1, 1, 1, 1, 1])

    def test_withdraw_failure_exact_change_not_possible(self):
        atm = ATM()
        atm.deposit([0, 0, 0, 1, 1])
        self.assertEqual(atm.withdraw(300), [-1])
        self.assertEqual(atm.banknotesTotal, [0, 0, 0, 1, 1])


if __name__ == '__main__':
    unittest.main()