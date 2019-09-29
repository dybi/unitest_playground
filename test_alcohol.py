from unittest import TestCase


def should_sell_alcohol(age: int) -> bool:
    return age >= 18


class TestShouldSellAlcohol(TestCase):
    def test_should_sell_when_user_is_18(self):
        # given
        user_age = 18

        # when
        result = should_sell_alcohol(user_age)

        # then
        self.assertEqual(result, True)
