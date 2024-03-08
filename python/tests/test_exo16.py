import unittest

def add_two_numbers(x, y):
    return x + y

def test_add_two_numbers():
    assert add_two_numbers(2, 3) == 5
    assert add_two_numbers(-1, 1) == 0
    assert add_two_numbers(-1, -1) == -2

def main():
    unittest.main()

if __name__ == "__main__":
    main()