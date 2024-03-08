
# Écrivez un programme en Python qui trouve l'intersection de deux ensembles


def intersection(ensemble1, ensemble2):
    result = ensemble1.intersection(ensemble2)
    return result

if __name__ == "__main__":
    ensemble1 = {1, 2, 3, 4, 5}
    ensemble2 = {4, 5, 6, 7, 8}
    resultat_intersection = intersection(ensemble1, ensemble2)
    print("Intersection des ensembles:", resultat_intersection)






