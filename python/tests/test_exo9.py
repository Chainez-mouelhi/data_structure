import unittest

def inverse_tuples(liste_tuples):
    tuples_inverses = []

    
    for t in liste_tuples:
        tuples_inverses.append(tuple(reversed(t)))

    return tuples_inverses

def test_inverse_tuples():
    liste_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    tuples_inverses = inverse_tuples(liste_tuples)
    resultat_attendu = [(3, 2, 1), (6, 5, 4), (9, 8, 7)]
    assert tuples_inverses == resultat_attendu, f"Expected {resultat_attendu} but got {tuples_inverses}"

test_inverse_tuples()