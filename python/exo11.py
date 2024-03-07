def trouver_plus_grand(a, b, c):
    return max(a, b, c)

def main():
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
    c = float(input("Entrez le troisième nombre : "))

    plus_grand = trouver_plus_grand(a, b, c)
    print("Le plus grand nombre est :", plus_grand)

if __name__ == "__main__":
    main()
