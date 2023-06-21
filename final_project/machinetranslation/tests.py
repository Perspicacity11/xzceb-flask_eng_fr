import unittest

from translator import english_to_french, french_to_english

class TranslationTest(unittest.TestCase):
    def test_eng2fr(self):
        self.assertEqual(english_to_french('Hello'), 'Pepitoooo')

    def test_fr2eng(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()