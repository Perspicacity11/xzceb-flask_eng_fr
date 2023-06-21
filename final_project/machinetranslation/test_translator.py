import unittest

from translator import english_to_french, french_to_english

class TranslationTest(unittest.TestCase):
    def test_eng2frEq(self):
        self.assertEqual(english_to_french('Waterfall'), 'Cascade')

    def test_eng2frNEq(self):
        self.assertNotEqual(english_to_french('Mountain'), 'Fromage')

    def test_fr2engEq(self):
        self.assertEqual(french_to_english('Rapproachment'), 'Reconciliation')

    def test_fr2engNEq(self):
        self.assertNotEqual(english_to_french('Cheese'), 'Montagne')

if __name__ == '__main__':
    unittest.main()