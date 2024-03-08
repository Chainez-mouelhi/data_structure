import unittest

from your_module import difference_symetrique # replace `your_module` with the actual name of the module

class TestDifferenceSymetrique(unittest.TestCase):
    def test_difference_symetrique(self):
        ensemble1 = {1, 2, 3, 4, 5}
        ensemble2 = {4, 5, 6, 7, 8}
        resultat_difference_symetrique = difference_symetrique(ensemble1, ensemble2)
        expected_result = {1, 2, 3, 6, 7, 8}
        self.assertEqual(resultat_difference_symetrique, expected_result)

if __name__ == '__main__':
    unittest.main()