def main():
    # Demander à l'utilisateur de saisir deux nombres sous forme de chaînes de caractères
    num1_str = input("Entrez le premier nombre : ")
    num2_str = input("Entrez le deuxième nombre : ")

    # Convertir les chaînes de caractères en entiers
    num1 = int(num1_str)
    num2 = int(num2_str)

    # Calculer la somme des deux nombres
    somme = num1 + num2

    # Afficher le résultat sous différentes formes
    print("La somme de", num1, "et", num2, "est :", somme)
    print("La somme de {} et {} est : {}".format(num1, num2, somme))
    print(f"La somme de {num1} et {num2} est : {somme}")

if __name__ == "__main__":
    main()
