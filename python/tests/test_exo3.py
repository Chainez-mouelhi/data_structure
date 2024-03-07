import unittest

def extrait_dernier_mot(chaine):
    mots = chaine.split()
    return mots[-1]

class TestExtraitDernierMot(unittest.TestCase):
    def test_extrait_dernier_mot(self):
        chaine = "Python est un langage de programmation puissant et facile à apprendre"
        resultat_attendu = "apprendre"
        self.assertEqual(extrait_dernier_mot(chaine), resultat_attendu)

if __name__ == '__main__':
    unittest.main()
