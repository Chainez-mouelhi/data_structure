import unittest

def extrait_mot_python(chaine):
    mots = chaine.split()
    if mots:
        return mots[0]
    else:
        return ""

class TestExtraitMotPython(unittest.TestCase):
    def test_extrait_mot_python(self):
        chaine = "Python est un langage de programmation puissant et facile à apprendre"
        resultat_attendu = "Python"
        self.assertEqual(extrait_mot_python(chaine), resultat_attendu)

    def test_extrait_mot_python_chaine_vide(self):
        chaine = ""
        resultat_attendu = ""
        self.assertEqual(extrait_mot_python(chaine), resultat_attendu)

    def test_extrait_mot_python_chaine_avec_un_mot(self):
        chaine = "Python"
        resultat_attendu = "Python"
        self.assertEqual(extrait_mot_python(chaine), resultat_attendu)

    def test_extrait_mot_python_chaine_avec_plusieurs_mots(self):
        chaine = "Python est super"
        resultat_attendu = "Python"
        self.assertEqual(extrait_mot_python(chaine), resultat_attendu)

        # Vérification de l'exactitude du résultat attendu
        self.assertEqual(resultat_attendu, "Python")

if __name__ == '__main__':
    unittest.main()
