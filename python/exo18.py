def difference_symetrique(ensemble1, ensemble2):
    return ensemble1.symmetric_difference(ensemble2)

ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

resultat_difference_symetrique = difference_symetrique(ensemble1, ensemble2)
print("Différence symétrique entre les ensembles:", resultat_difference_symetrique)
