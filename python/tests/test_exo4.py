import unittest

def inverse_chaine(chaine):
    size = len(chaine)
    chaine_inverse = ""
    for i in range(size - 1, -1, -1):
        chaine_inverse += chaine[i]
    return chaine_inverse

class TestInverseChaine(unittest.TestCase):
    def test_inverse_chaine(self):
        chaine = "Python est un langage de programmation puissant et facile à apprendre"
        resultat_attendu = "erdnerpa à elicaf te tnussiappa ed gnimmargorp ed egagnal nu tnu siuqnoil"
        self.assertEqual(inverse_chaine(chaine), resultat_attendu)

if __name__ == '__main__':
    unittest.main()
