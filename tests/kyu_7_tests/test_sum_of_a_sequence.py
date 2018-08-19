
import unittest

from katas.kyu_7.sum_of_a_sequence import sequence_sum


class EvenOrOddTestCases(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sequence_sum(2, 6, 2), 12)

    def test_equals_2(self):
        self.assertEqual(sequence_sum(1, 5, 1), 15)

    def test_equals_3(self):
        self.assertEqual(sequence_sum(16, 15, 3), 0)
