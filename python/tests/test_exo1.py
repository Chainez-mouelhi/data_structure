import unittest

def compter_majuscules_minuscules(chaine):
    majuscules = 0
    minuscules = 0

    for caractere in chaine:
        if caractere.isupper():
            majuscules += 1
        elif caractere.islower():
            minuscules += 1

    return majuscules, minuscules

def test_compter_majuscules_minuscules():
    resultat_attendu_majuscules = 2
    resultat_attendu_minuscules = 3
    chaine = "AbCdEf"
    majuscules, minuscules = compter_majuscules_minuscules(chaine)
    assert majuscules == resultat_attendu_majuscules, f"Expected {resultat_attendu_majuscules} but got {majuscules}"
    assert minuscules == resultat_attendu_minuscules, f"Expected {resultat_attendu_minuscules} but got {minuscules}"

test_compter_majuscules_minuscules()