
import unittest

from katas.kyu_8.opposite_number import opposite


class OppositeNumberTestCases(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(opposite(1), -1)

    def test_equals_2(self):
        self.assertEqual(opposite(14), -14)

    def test_equals_3(self):
        self.assertEqual(opposite(-34), 34)
