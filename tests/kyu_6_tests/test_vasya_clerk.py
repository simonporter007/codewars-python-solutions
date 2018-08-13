
import unittest

from katas.kyu_6.vasya_clerk import tickets


class VasyaClerkTestCases(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(tickets([25, 25, 50]), "YES")

    def test_equals_2(self):
        self.assertEqual(tickets([25, 100]), "NO")

    def test_equals_3(self):
        self.assertEqual(tickets([25, 25, 50, 50, 100]), "NO")

    def test_equals_4(self):
        self.assertEqual(tickets([50, 25, 50, 50, 100]), "NO")

    def test_equals_5(self):
        self.assertEqual(tickets([25, 25, 25, 50, 25, 100]), "YES")

    def test_equals_6(self):
        self.assertEqual(tickets([25]), "YES")

    def test_equals_7(self):
        self.assertEqual(tickets([50]), "NO")

    def test_equals_8(self):
        self.assertEqual(
            tickets([25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]), "NO")

    def test_equals_9(self):
        self.assertEqual(tickets([25, 25, 25, 25, 50, 100, 50]), "YES")
