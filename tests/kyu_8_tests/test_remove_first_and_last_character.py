
import unittest

from katas.kyu_8.remove_first_and_last_character import remove_char


class RemoveFirstOrLastCharacterTestCases(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(remove_char("eloquent"), "loquen")

    def test_equals_2(self):
        self.assertEqual(remove_char("country"), "ountr")

    def test_equals_3(self):
        self.assertEqual(remove_char("ok"), "")
