import unittest
from unittest import TestCase
from unittest.mock import Mock, PropertyMock, patch

from parameterized import parameterized

from entities import Account, User, TransferImpossible, make_money_transfer


class TestUser(TestCase):
    def test_give_me_the_money_should_return_available_funds_from_all_accounts(self):
        # account_1 = Mock()
        # type(account_1).balance = PropertyMock(return_value=50)
        # account_2 = Mock()
        # type(account_2).balance = PropertyMock(return_value=100)
        account_1 = Mock()
        account_1.get_balance.return_value = 50
        account_2 = Mock()
        account_2.get_balance.return_value = 100

        user = User("Janusz", 40, [account_1, account_2])

        self.assertEqual(user.give_me_the_money(), 150)

    @parameterized.expand([
        ([], 0),
        ([Mock(get_balance=Mock(return_value=500))], 500),
        (
            [
                Mock(get_balance=Mock(return_value=100)),
                Mock(get_balance=Mock(return_value=300)),
                Mock(get_balance=Mock(return_value=7)),
            ],
            407
        ),
    ])
    def test_give_me_the_money(self, accounts, expected_amount):
        user = User("Janusz", 40, accounts)

        self.assertEqual(user.give_me_the_money(), expected_amount)


class TestAccount(TestCase):
    def test_transfer_should_send_money_to_other_account(self):
        account = Account()
        other_account = Mock()

        yogurt_price = 1.29
        account.transfer(other_account, yogurt_price)

        other_account.add_funds.assert_called_once_with(yogurt_price)

    # def test_setting_balance_below_zero_should_raise_value_error(self):
    #     account = Account()
    #     with self.assertRaises(ValueError):
    #         account.balance -= 1

    def test_id_is_generated_properly(self):
        generated_id = 777
        with patch('entities.randint', return_value=generated_id):
            account = Account()
            self.assertEqual(account.get_id(), generated_id)


class TestMakeMoneyTransfer(TestCase):
    def test_should_raise_transfer_impossible_when_transfer_fails(self):
        account_1 = Mock()
        account_1.transfer.side_effect = TransferImpossible
        account_2 = Mock()

        with self.assertRaises(TransferImpossible):
            make_money_transfer(account_1, account_2, 100)


if __name__ == "__main__":
    unittest.main()    
