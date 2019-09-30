from unittest import TestCase
from unittest.mock import Mock

from entities import Account, User


class TestUser(TestCase):
    def test_give_me_the_money_should_return_available_funds_from_all_accounts(self):
        account_1 = Mock()
        account_1.get_balance.return_value = 50
        account_2 = Mock()
        account_2.get_balance.return_value = 100

        user = User("Janusz", 40, [account_1, account_2])

        self.assertEqual(user.give_me_the_money(), 150)
