chaine = "Python est un langage de programmation puissant et facile à apprendre"
size  = len(chaine)

chaine_inverse = ""
for i in range(size-1,-1,-1):
    chaine_inverse += chaine[i]
print(chaine_inverse)