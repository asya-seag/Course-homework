
import unittest

from isogram_f import isogram


class TestIsogram(unittest.TestCase):
    #testing that our function gives us True statement when we enter isogram
    def test_isogram(self):
        self.assertTrue(isogram("isogram"))
        self.assertTrue(isogram("uncopyrightable"))
        self.assertTrue(isogram("ambidextrously”"))


    #testing that we get False when word isn't and isogram
    def test_isogram_2(self):
        self.assertFalse(isogram("madam"))
        self.assertFalse(isogram("tintin"))
        self.assertFalse(isogram("simmetry"))

if __name__ == '__main__':
    unittest.main()