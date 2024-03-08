import unittest

def filtrer_notes(mon_dict):
    new_dict = {}
    for name, note in mon_dict.items():
        if note >= 15:
            new_dict[name] = note
    return new_dict

def test_filtrer_notes():
    # Test with a dictionary containing only students with notes above 15
    resultat_attendu = {"Nono": 19, "Hugo": 20}
    mon_dict = {"Alice": 16, "Albert": 13, "Tom": 12, "Nono": 19, "Hugo": 20}
    assert filtrer_notes(mon_dict) == resultat_attendu

    # Test with a dictionary containing only students with notes below 15
    resultat_attendu = {}
    mon_dict = {"Alice": 14, "Albert": 13, "Tom": 12, "Nono": 11, "Hugo": 10}
    assert filtrer_notes(mon_dict) == resultat_attendu

    # Test with an empty dictionary
    resultat_attendu = {}
    mon_dict = {}
    assert filtrer_notes(mon_dict) == resultat_attendu

def main():
    mon_dict = {"Alice": 16, "Albert": 13, "Tom": 12, "Nono": 19, "Hugo": 20}
    new_dict = filtrer_notes(mon_dict)
    print(new_dict)

if __name__ == "__main__":
    main()