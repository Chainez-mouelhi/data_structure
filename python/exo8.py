def tuple_max_elements(tuple_list):
    max_tuple = max(tuple_list, key=len)
    return max_tuple

# Exemple d'utilisation
tuple_list = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]
max_tuple = tuple_max_elements(tuple_list)
print("Le tuple avec le plus d'éléments est :", max_tuple)
