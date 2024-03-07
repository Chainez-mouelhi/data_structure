def est_palindrome(mot):
    """Vérifie si un mot est un palindrome."""
    return mot == mot[::-1]

def compter_palindromes(liste_mots):
    """Compte le nombre de mots palindromes dans une liste."""
    count = 0
    for mot in liste_mots:
        if est_palindrome(mot):
            count += 1
    return count

# Exemple d'utilisation
liste_mots = ["radar", "kayak", "tenet", "hello", "world"]
nombre_palindromes = compter_palindromes(liste_mots)
print("Nombre de mots palindromes :", nombre_palindromes)
