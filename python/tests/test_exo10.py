import unittest
import io
import sys

def afficher_pyramide(hauteur):
    for i in range(1, hauteur + 1):
        print(" " * (hauteur - i) + "*" * (2 * i - 1))

def test_afficher_pyramide():
    capture = io.StringIO()
    sys.stdout = capture
    hauteur = 5
    afficher_pyramide(hauteur)
    resultat_attendu = "    *\n   ***\n  *****\n *******\n*********\n"
    assert capture.getvalue() == resultat_attendu, f"Expected {resultat_attendu} but got {capture.getvalue()}"
    sys.stdout = sys.__stdout__

test_afficher_pyramide()