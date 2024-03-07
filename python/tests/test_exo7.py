import unittest
from io import StringIO
import sys

def rotate_list(input_list, rotations):
    rotated_list = input_list[int(rotations):] + input_list[0:int(rotations)]
    return rotated_list

class TestRotateList(unittest.TestCase):

    def test_rotate_list(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rotations = "3"
        expected_output = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        self.assertEqual(rotate_list(input_list, rotations), expected_output)

    def test_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        rotations = "3"
        expected_output = "[4, 5, 6, 7, 8, 9, 1, 2, 3]\n"
        print(rotate_list(input_list, rotations))  # Ajout de cette ligne pour afficher la liste tournée
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
