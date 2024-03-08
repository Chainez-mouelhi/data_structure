

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
    
   

test_compter_majuscules_minuscules()