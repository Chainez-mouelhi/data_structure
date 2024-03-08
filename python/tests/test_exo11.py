import unittest

def trouver_plus_grand(a, b, c):
    return max(a, b, c)

def test_trouver_plus_grand():
    resultat_attendu = 3
    assert trouver_plus_grand(1, 2, 3) == resultat_attendu, f"Expected {resultat_attendu} but got {trouver_plus_grand(1, 2, 3)}"

test_trouver_plus_grand()