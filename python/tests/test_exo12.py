import unittest

def decoder_message(message):
    if not message:
        return ""

    try:
        # Diviser la chaîne en une liste de nombres
        codes = message.split()

        # Convertir chaque nombre en son caractère ASCII correspondant
        decoded_message = "".join(chr(int(code)) for code in codes)

        return decoded_message
    except ValueError:
        return "Erreur: la chaîne contient des caractères non valides"

class TestDecoderMessage(unittest.TestCase):
    def test_decoder_message_vide(self):
        self.assertEqual(decoder_message(""), "")

    def test_decoder_message_simple(self):
        self.assertEqual(decoder_message("83 69 67"), "SEC")

    def test_decoder_message_avec_erreur(self):
        self.assertEqual(decoder_message("83 69 ABC"), "Erreur: la chaîne contient des caractères non valides")

if __name__ == "__main__":
    unittest.main()
