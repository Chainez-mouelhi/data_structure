import unittest

def test_liste():
    liste = [1, 1, 2, 2, 2, 2, 2, 2, 2]
    liste2 = []
    for nombre in liste:
        if nombre not in liste2:
            liste2.append(nombre)
    resultat_attendu = [1, 2]
    assert liste2 == resultat_attendu, f"Expected {resultat_attendu} but got {liste2}"

test_liste()