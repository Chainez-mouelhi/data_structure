import unittest

def filter_notes(mon_dict):
    new_dict = {}
    for name, note in mon_dict.items():
        if note >= 15:
            new_dict[name] = note
    return new_dict

class TestFilterNotes(unittest.TestCase):
    def test_filter_notes(self):
        mon_dict = {"Alice": 16, "Albert": 13, "Tom": 12, "Nono": 19, "Hugo": 20}
        expected_result = {"Alice": 16, "Nono": 19, "Hugo": 20}
        self.assertDictEqual(filter_notes(mon_dict), expected_result)

    def test_empty_input(self):
        mon_dict = {}
        expected_result = {}
        self.assertDictEqual(filter_notes(mon_dict), expected_result)

    def test_no_notes_above_15(self):
        mon_dict = {"Alice": 14, "Bob": 13, "Charlie": 12}
        expected_result = {}
        self.assertDictEqual(filter_notes(mon_dict), expected_result)

    def test_all_notes_above_15(self):
        mon_dict = {"Alice": 16, "Bob": 17, "Charlie": 18}
        expected_result = {"Alice": 16, "Bob": 17, "Charlie": 18}
        self.assertDictEqual(filter_notes(mon_dict), expected_result)

if __name__ == '__main__':
    unittest.main()
