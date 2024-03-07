def est_palindrome(mot):
    return mot == mot[::-1]

def compter_palindromes(liste_mots):
    count = 0
    for mot in liste_mots:
        if est_palindrome(mot):
            count += 1
    return count

def main():
    liste_mots = input("Entrez une liste de mots séparés par des espaces : ").split()
    nombre_palindromes = compter_palindromes(liste_mots)
    print("Nombre de mots palindromes :", nombre_palindromes)

if __name__ == "__main__":
    main()
