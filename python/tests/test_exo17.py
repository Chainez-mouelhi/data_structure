import unittest

def intersection(ensemble1, ensemble2):
    result = ensemble1.intersection(ensemble2)
    return result

class TestIntersectionFunction(unittest.TestCase):
    def test_intersection(self):
        ensemble1 = {1, 2, 3, 4, 5}
        ensemble2 = {4, 5, 6, 7, 8}
        result = intersection(ensemble1, ensemble2)
        expected_result = {4, 5}
        self.assertEqual(result, expected_result)

    def test_empty_intersection(self):
        ensemble1 = {1, 2, 3}
        ensemble2 = {4, 5, 6}
        result = intersection(ensemble1, ensemble2)
        expected_result = set()
        self.assertEqual(result, expected_result)

    def test_identical_sets(self):
        ensemble1 = {1, 2, 3}
        ensemble2 = {1, 2, 3}
        result = intersection(ensemble1, ensemble2)
        expected_result = {1, 2, 3}
        self.assertEqual(result, expected_result)

    def test_no_common_elements(self):
        ensemble1 = {1, 2, 3}
        ensemble2 = {4, 5, 6}
        result = intersection(ensemble1, ensemble2)
        expected_result = set()
        self.assertEqual(result, expected_result)

    def test_empty_sets(self):
        ensemble1 = set()
        ensemble2 = set()
        result = intersection(ensemble1, ensemble2)
        expected_result = set()
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
