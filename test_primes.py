import unittest

from parameterized import parameterized

from primes import is_prime


class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    @parameterized.expand([
        (2,),
        (3,),
        (5,),
        (7,),
        (11,),
        (19,),
    ])
    def test_is_prime(self, number):
        self.assertTrue(is_prime(number))

    @parameterized.expand([
        (4,),
        (6,),
        (9,),
        (0,),
        (-1,),
    ])
    def test_is_non_prime(self, number):
        self.assertFalse(is_prime(number))


if __name__ == '__main__':
    unittest.main()
