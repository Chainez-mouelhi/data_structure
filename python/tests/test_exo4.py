import unittest
def inverse_chaine(chaine):
    chaine_inverse = chaine[::-1]
    return chaine_inverse

class TestInverseChaine(unittest.TestCase):
    def test_inverse_chaine(self):
        chaine = "Python est un langage de programmation puissant et facile à apprendre"
        resultat_attendu = "erdnerppa à elicaf te tnassiup noitammargorp ed egagnal nu tse nohtyP"
        self.assertEqual(inverse_chaine(chaine), resultat_attendu)

if __name__ == '__main__':
    unittest.main()

