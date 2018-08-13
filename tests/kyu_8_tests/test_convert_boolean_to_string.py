
import unittest

from katas.kyu_8.convert_boolean_to_string import bool_to_word


class BoolToWordTestCases(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(bool_to_word(True), "Yes")

    def test_equals_2(self):
        self.assertEqual(bool_to_word(False), "No")
