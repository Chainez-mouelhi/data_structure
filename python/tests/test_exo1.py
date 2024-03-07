import unittest

class TestLettre(unittest.TestCase):

    def testcountmajuscule(self):
        self.assertEqual(count_letters("OK"), 2)

    def testcount_minuscule(self):
        minuscules = count_letters("ok")
        self.assertEqual(minuscules, 0)

def count_letters(chaine):
    majuscules = 0

    for caractere in chaine:
        if caractere.isupper():
            majuscules += 1

    return majuscules

if __name__ == '__main__':
    unittest.main()

