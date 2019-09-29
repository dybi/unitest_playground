import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        # given
        s = 'hello world'

        # when
        result = s.split()

        # then
        self.assertEqual(result, ['hello', 'world'])

    def test_split_raises_type_error_on_wrong_type(self):
        # given
        s = "some string"

        # when / then
        with self.assertRaises(TypeError):
            s.split(2)

