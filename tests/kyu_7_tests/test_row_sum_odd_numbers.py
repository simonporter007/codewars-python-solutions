import unittest

from katas.kyu_7.row_sum_odd_numbers import row_sum_odd_numbers


class RowSumOddNumbersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(row_sum_odd_numbers(1), 1)

    def test_equals_2(self):
        self.assertEqual(row_sum_odd_numbers(2), 8)

    def test_equals_3(self):
        self.assertEqual(row_sum_odd_numbers(3), 27)

    def test_equals_4(self):
        self.assertEqual(row_sum_odd_numbers(13), 2197)
