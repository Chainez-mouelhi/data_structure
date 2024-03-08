import unittest

def extrait_mot_python(chaine):
    mots = chaine.split()
    if mots:
        return mots[0]
    else:
        return ""

def test_extrait_mot_python_specific_case():
    chaine = "Python est un langage de programmation puissant et facile à apprendre"
    resultat_attendu = "Python"
    assert extrait_mot_python(chaine) == resultat_attendu, f"Expected {resultat_attendu} but got {extrait_mot_python(chaine)}"

def test_extrait_mot_python_empty_case():
    chaine = ""
    resultat_attendu = ""
    assert extrait_mot_python(chaine) == resultat_attendu, f"Expected {resultat_attendu} but got {extrait_mot_python(chaine)}"

test_extrait_mot_python_specific_case()
test_extrait_mot_python_empty_case()