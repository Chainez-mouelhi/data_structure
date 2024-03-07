import unittest

def extrait_mot_python(chaine):
    mots = chaine.split()
    return mots[0]

class TestExtraitMotPython(unittest.TestCase):
    def test_extrait_mot_python(self):
        chaine = "Python est un langage de programmation puissant et facile à apprendre"
        resultat_attendu = "Python"
        self.assertEqual(extrait_mot_python(chaine), resultat_attendu)

if __name__ == '__main__':
    unittest.main()
