import unittest

def est_palindrome(mot):
    return mot == mot[::-1]

def compter_palindromes(liste_mots):
    count = 0
    for mot in liste_mots:
        if est_palindrome(mot):
            count += 1
    return count

def test_compter_palindromes():
    resultat_attendu = 2
    liste_mots = "kayak radar".split()
    assert compter_palindromes(liste_mots) == resultat_attendu, f"Expected {resultat_attendu} but got {compter_palindromes(liste_mots)}"

test_compter_palindromes()