import unittest

def trouver_plus_grand(a, b, c):
    return max(a, b, c)

class TestTrouverPlusGrand(unittest.TestCase):
    def test_trouver_plus_grand_a_est_plus_grand(self):
        self.assertEqual(trouver_plus_grand(3, 2, 1), 3)

    def test_trouver_plus_grand_b_est_plus_grand(self):
        self.assertEqual(trouver_plus_grand(1, 3, 2), 3)

    def test_trouver_plus_grand_c_est_plus_grand(self):
        self.assertEqual(trouver_plus_grand(1, 2, 3), 3)

    def test_trouver_plus_grand_tous_egales(self):
        self.assertEqual(trouver_plus_grand(1, 1, 1), 1)

if __name__ == "__main__":
    unittest.main()
