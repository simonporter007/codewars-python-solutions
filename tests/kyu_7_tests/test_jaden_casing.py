import unittest

from katas.kyu_7.jaden_casing import toJadenCase


class ToJadenCaseTestCases(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(toJadenCase("How can mirrors be real if our eyes aren't real"),
                         "How Can Mirrors Be Real If Our Eyes Aren't Real")

    def test_equals_2(self):
        self.assertEqual(toJadenCase("How can mirrors be Real if Our eyes aren't real"),
                         "How Can Mirrors Be Real If Our Eyes Aren't Real")

    def test_equals_3(self):
        self.assertEqual(toJadenCase("testing a string by jaden smith"),
                         "Testing A String By Jaden Smith")
