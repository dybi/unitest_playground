from contextlib import suppress
from unittest.mock import Mock


class TransferImpossibleException(Exception):
    pass


class NoFunds(TransferImpossibleException):
    pass


class AccountLocked(TransferImpossibleException):
    pass


def foo(account):
    with suppress(ZeroDivisionError):
        account.transfer()


mocked_account = Mock()
mocked_account.transfer.side_effect = ZeroDivisionError

print("-" * 10)
foo(mocked_account)
print("-" * 10)
pass
