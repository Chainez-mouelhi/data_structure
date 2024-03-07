import unittest

def inverse_tuples(liste_tuples):
    tuples_inverses = []
    for t in liste_tuples:
        tuples_inverses.append(tuple(reversed(t)))
    return tuples_inverses

class TestInverseTuples(unittest.TestCase):
    def test_inverse_tuples(self):
        liste_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        resultat_attendu = [(3, 2, 1), (6, 5, 4), (9, 8, 7)]
        self.assertEqual(inverse_tuples(liste_tuples), resultat_attendu)

if __name__ == "__main__":
    unittest.main()
