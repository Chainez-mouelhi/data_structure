import unittest
import io
import sys

def main():
    num1_str = input("Entrez le premier nombre : ")
    num2_str = input("Entrez le deuxième nombre : ")
    num1 = int(num1_str)
    num2 = int(num2_str)
    somme = num1 + num2
    print("La somme de", num1, "et", num2, "est :", somme)
    print("La somme de {} et {} est : {}".format(num1, num2, somme))
    print(f"La somme de {num1} et {num2} est : {somme}")

def test_main():
    sys.stdin = io.StringIO("3\n5\n")
    sys.stdout = io.StringIO()
    main()
    sys.stdout.seek(0)
    expected_output = sys.stdout.read()
    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__
    assert expected_output == "La somme de 3 et 5 est : 8\nLa somme de 3 et 5 est : 8\nLa somme de 3 et 5 est : 8\n", f"Expected {expected_output} but got {sys.stdout.getvalue()}"

test_main()