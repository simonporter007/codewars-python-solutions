
import unittest

from katas.kyu_8.return_negative import make_negative


class MakeNegativeTestCases(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(make_negative(0), 0)

    def test_equals_2(self):
        self.assertEqual(make_negative(1), -1)

    def test_equals_3(self):
        self.assertEqual(make_negative(-2), -2)
