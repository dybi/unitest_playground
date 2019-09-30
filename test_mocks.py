from unittest import TestCase

from entities import Account, User


class TestUser(TestCase):
    def test_give_me_the_money_should_return_available_funds_from_all_accounts(self):
        account_1 = Account()
        account_1.add_funds(50)
        account_2 = Account()
        account_2.add_funds(100)

        user = User("Janusz", 40, [account_1, account_2])

        self.assertEqual(user.give_me_the_money(), 150)
