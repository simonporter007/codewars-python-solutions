
import unittest

from katas.kyu_8.sum_of_positive import positive_sum


class PositiveSumTestCases(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(positive_sum([1, 2, 3, 4, 5]), 15)

    def test_equals_2(self):
        self.assertEqual(positive_sum([1, -2, 3, 4, 5]), 13)

    def test_equals_3(self):
        self.assertEqual(positive_sum([-1, 2, 3, 4, -5]), 9)

    def test_equals_4(self):
        self.assertEqual(positive_sum([]), 0)

    def test_equals_5(self):
        self.assertEqual(positive_sum([-1, -2, -3, -4, -5]), 0)
