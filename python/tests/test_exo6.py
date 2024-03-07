import unittest

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        input_list = [1, 1, 2, 2, 2, 2, 2, 2, 2]
        expected_output = [1, 2]
        self.assertEqual(remove_duplicates(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()
