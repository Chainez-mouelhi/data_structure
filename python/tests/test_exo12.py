import unittest

def decoder_message(message):
    # Diviser la chaîne en une liste de nombres
    codes = message.split()

    # Convertir chaque nombre en son caractère ASCII correspondant
    decoded_message = "".join(chr(int(code)) for code in codes)

    return decoded_message

def test_decoder_message():
    resultat_attendu = "Hello, world!"
    message = "72 101 108 108 111 44 32 119 111 114 108 100 33"
    assert decoder_message(message) == resultat_attendu, f"Expected {resultat_attendu} but got {decoder_message(message)}"

test_decoder_message()