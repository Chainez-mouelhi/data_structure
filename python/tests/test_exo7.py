import unittest

def test_new_liste():
    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = "3"
    new_liste = liste[int(x):] + liste[0:int(x)]
    resultat_attendu = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    assert new_liste == resultat_attendu, f"Expected {resultat_attendu} but got {new_liste}"

test_new_liste()