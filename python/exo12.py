def decoder_message(message):
    # Diviser la chaîne en une liste de nombres
    codes = message.split()

    # Convertir chaque nombre en son caractère ASCII correspondant
    decoded_message = "".join(chr(int(code)) for code in codes)

    return decoded_message

def main():
    message = input("Entrez le message codé : ")
    decoded_message = decoder_message(message)
    print("Message décodé :", decoded_message)

if __name__ == "__main__":
    main()
