import unittest

def est_palindrome(mot):
    """Vérifie si un mot est un palindrome."""
    return mot == mot[::-1]

def compter_palindromes(liste_mots):
    """Compte le nombre de mots palindromes dans une liste."""
    count = 0
    for mot in liste_mots:
        if est_palindrome(mot):
            count += 1
    return count

class TestPalindrome(unittest.TestCase):
    def test_est_palindrome(self):
        self.assertTrue(est_palindrome("radar"))
        self.assertTrue(est_palindrome("kayak"))
        self.assertTrue(est_palindrome("tenet"))
        self.assertFalse(est_palindrome("hello"))
        self.assertFalse(est_palindrome("world"))

    def test_compter_palindromes(self):
        liste_mots = ["radar", "kayak", "tenet", "hello", "world"]
        self.assertEqual(compter_palindromes(liste_mots), 3)

if __name__ == "__main__":
    unittest.main()
