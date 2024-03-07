import unittest
from unittest.mock import patch
import io
import sys

def main():
    # Demander à l'utilisateur de saisir deux nombres sous forme de chaînes de caractères
    num1_str = input("Entrez le premier nombre : ")
    num2_str = input("Entrez le deuxième nombre : ")

    # Convertir les chaînes de caractères en entiers
    num1 = int(num1_str)
    num2 = int(num2_str)

    # Calculer la somme des deux nombres
    somme = num1 + num2

    # Afficher le résultat sous différentes formes
    print("La somme de", num1, "et", num2, "est :", somme)
    print("La somme de {} et {} est : {}".format(num1, num2, somme))
    print(f"La somme de {num1} et {num2} est : {somme}")

class TestSumFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['5', '7'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sum_output(self, mock_stdout, mock_input):
        expected_output = "La somme de 5 et 7 est : 12\nLa somme de 5 et 7 est : 12\nLa somme de 5 et 7 est : 12\n"
        main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['5', '7'])
    def test_sum(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            expected_output = "La somme de 5 et 7 est : 12\nLa somme de 5 et 7 est : 12\nLa somme de 5 et 7 est : 12\n"
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
