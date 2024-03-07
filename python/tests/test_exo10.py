import unittest
from io import StringIO
import sys

def afficher_pyramide(hauteur):
    for i in range(1, hauteur + 1):
        print(" " * (hauteur - i) + "*" * (2 * i - 1))

class TestPyramide(unittest.TestCase):
    def test_afficher_pyramide(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        afficher_pyramide(3)
        output = captured_output.getvalue()
        self.assertEqual(output, "  *\n ***\n*****\n")

        sys.stdout = sys.__stdout__  # Reset redirect.

if __name__ == "__main__":
    unittest.main()
