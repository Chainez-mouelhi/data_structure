import unittest

class TestLettre(unittest.TestCase):

    def testcountmajuscule(self):
        self.assertEqual(count_letters("OK"), 2)

    def testcount_minuscule(self):
        self.assertEqual(count_letters("ok"), 2)



def count_letters(chaine):
    majuscules = 0
    minuscules = 0

    for caractere in chaine:
        if caractere.isupper():
            majuscules += 1
        elif caractere.islower():
            minuscules += 1

    return majuscules, minuscules

if __name__ == '__main':
    unittest.main()