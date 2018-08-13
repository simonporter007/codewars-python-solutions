
import unittest

from katas.kyu_7.descending_order import Descending_Order


class DescendingOrderTestCases(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Descending_Order(21445), 54421)

    def test_equals_2(self):
        self.assertEqual(Descending_Order(145263), 654321)

    def test_equals_3(self):
        self.assertEqual(Descending_Order(1254859723), 9875543221)
