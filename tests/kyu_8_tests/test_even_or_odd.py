
import unittest

from katas.kyu_8.even_or_odd import even_or_odd


class EvenOrOddTestCases(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(even_or_odd(0), "Even")

    def test_equals_2(self):
        self.assertEqual(even_or_odd(1), "Odd")

    def test_equals_3(self):
        self.assertEqual(even_or_odd(2), "Even")
