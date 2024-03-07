import unittest

def tuple_max_elements(tuple_list):
    sorted_tuples = sorted(tuple_list, key=len, reverse=True)
    return sorted_tuples[0]

class TestTupleMaxElements(unittest.TestCase):
    def test_tuple_max_elements(self):
        tuple_list = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
        resultat_attendu = (7, 8, 9, 10)
        self.assertEqual(tuple_max_elements(tuple_list), resultat_attendu)

if __name__ == "__main__":
    unittest.main()
