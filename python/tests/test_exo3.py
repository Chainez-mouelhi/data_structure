import unittest

def extrait_dernier_mot(chaine):
    mots = chaine.split()
    return mots[-1]

def test_extrait_dernier_mot_specific_case():
    chaine = "Python est un langage de programmation puissant et facile à apprendre"
    resultat_attendu = "apprendre"
    assert extrait_dernier_mot(chaine) == resultat_attendu, f"Expected {resultat_attendu} but got {extrait_dernier_mot(chaine)}"

def test_extrait_dernier_mot_empty_case():
    chaine = ""
    resultat_attendu = ""
    assert extrait_dernier_mot(chaine) == resultat_attendu, f"Expected {resultat_attendu} but got {extrait_dernier_mot(chaine)}"

test_extrait_dernier_mot_specific_case()
test_extrait_dernier_mot_empty_case()