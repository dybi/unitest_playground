from random import randint
from typing import List, Optional


def generate_id() -> int:
    # return some number, let's assume some complicated calculations
    return randint(0, 999)


class Account:
    _id: int
    _balance: float

    def __init__(self) -> None:
        self._id = generate_id()
        self._balance = 0

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        current = self.balance
        if current + value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def add_funds(self, value: float) -> None:
        # adding the balance in banking transaction system
        self._balance += value

    def get_id(self) -> int:
        return self._id

    def transfer(self, other_account: 'Account', value: float) -> None:
        # reducing the balance in banking transaction system
        self._balance -= value
        other_account.add_funds(value)


class User:
    name: str
    age: int
    accounts: List[Account]

    def __init__(
        self,
        name: str,
        age: int,
        accounts: Optional[List[Account]] = None,
    ) -> None:
        self.name = name
        self.age = age
        self.accounts: List[Account] = accounts if accounts is not None else []

    def give_me_the_money(self) -> float:
        available_funds = 0.0
        for account in self.accounts:
            available_funds += account.balance
        return available_funds

