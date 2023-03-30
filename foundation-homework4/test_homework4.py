import unittest

def final_price_sum(price):
    return 0 + price

class Testfinal_price_sum(unittest.TestCase):
    def test75(self):
        self.assertEqual(final_price_sum(75), 75, "Good to go")

    def test55(self):
        self.assertEqual(final_price_sum(55), 55, "Good to go")
    def test120(self):
        self.assertEqual(final_price_sum(120), 135, "Wrong result")



import unittest


class TestWordsForDictionary(unittest.TestCase):
    def test_negative(self):
        word = 'jeans'
        word_from_dictionary = 'dress, shirt, skirt, coat'
        message = "key is not in container."
        self.assertIn(word, word_from_dictionary, message)



import unittest


class TestWordinDictionary(unittest.TestCase):
    def test_positive(self):
        word = 'skirt'
        word_from_dictionary = 'dress, shirt, skirt, coat'
        message = "Word is in the dictionary."
        self.assertIn(word, word_from_dictionary, message)