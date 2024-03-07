import unittest
from unittest.mock import patch
from io import StringIO

# Définition des fonctions est_palindrome et compter_palindromes directement ici
def est_palindrome(mot):
    return mot == mot[::-1]

def compter_palindromes(liste_mots):
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

    @patch('builtins.input', return_value="radar kayak tenet hello world")
    @patch('sys.stdout', new_callable=StringIO)
    def test_compter_palindromes(self, mock_stdout, mock_input):
        mots = mock_input().split()  # Utiliser mock_input() directement
        self.assertEqual(compter_palindromes(mots), 3)
        mock_stdout.seek(0)
        self.assertEqual(mock_stdout.read().strip(), "Nombre de mots palindromes : 3")

if __name__ == "__main__":
    unittest.main()
