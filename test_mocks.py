from unittest import TestCase
from unittest.mock import Mock

from entities import Account, User


class TestUser(TestCase):
    def test_give_me_the_money_should_return_available_funds_from_all_accounts(self):
        account_1 = Mock()
        account_1.balance.return_value = 50
        account_2 = Mock()
        account_2.balance.return_value = 100

        user = User("Janusz", 40, [account_1, account_2])

        self.assertEqual(user.give_me_the_money(), 150)


class TestAccount(TestCase):
    def test_transfer_should_send_money_to_other_account(self):
        account = Account()
        other_account = Mock()

        yogurt_price = 1.29
        account.transfer(other_account, yogurt_price)

        other_account.add_funds.assert_called_once_with(yogurt_price)
