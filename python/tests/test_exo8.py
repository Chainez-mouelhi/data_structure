import unittest

def tuple_max_elements(tuple_list):
    max_tuple = max(tuple_list, key=len)
    return max_tuple

def test_tuple_max_elements():
    tuple_list = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
    max_tuple = tuple_max_elements(tuple_list)
    resultat_attendu = (7, 8, 9, 10)
    assert max_tuple == resultat_attendu, f"Expected {resultat_attendu} but got {max_tuple}"

test_tuple_max_elements()