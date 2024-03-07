def inverse_tuples(liste_tuples):
    # Créer une liste vide pour stocker les tuples inversés
    tuples_inverses = []

    # Parcourir chaque tuple dans la liste de tuples
    for t in liste_tuples:
        # Inverser l'ordre des éléments dans le tuple et l'ajouter à la liste de tuples inversés
        tuples_inverses.append(tuple(reversed(t)))

    return tuples_inverses

# Exemple d'utilisation
liste_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
tuples_inverses = inverse_tuples(liste_tuples)
print("Liste de tuples inversés :", tuples_inverses)
