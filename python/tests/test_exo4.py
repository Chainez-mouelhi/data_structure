import unittest

def inverse_chaine(chaine):
    size = len(chaine)
    chaine_inverse = ""
    for i in range(size):
        chaine_inverse += chaine[size-1-i]
    return chaine_inverse

def test_inverse_chaine_specific_case():
    chaine = "Python est un langage de programmation puissant et facile à apprendre"
    resultat_attendu = "erendreà éli facile étiliagnap gnidapmocorp gnitnes uB"
    assert inverse_chaine(chaine) == resultat_attendu, f"Expected {resultat_attendu} but got {inverse_chaine(chaine)}"

def test_inverse_chaine_empty_case():
    chaine = ""
    resultat_attendu = ""
    assert inverse_chaine(chaine) == resultat_attendu, f"Expected {resultat_attendu} but got {inverse_chaine(chaine)}"

test_inverse_chaine_specific_case()
test_inverse_chaine_empty_case()