def afficher_pyramide(hauteur):
    for i in range(1, hauteur + 1):
        print(" " * (hauteur - i) + "*" * (2 * i - 1))

def main():
    hauteur = int(input("Entrez la hauteur de la pyramide : "))
    afficher_pyramide(hauteur)

if __name__ == "__main__":
    main()
