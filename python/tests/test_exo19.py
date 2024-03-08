import unittest

class TestByteArray(unittest.TestCase):
    def test_creation(self):
        entiers = [1, 2, 3, 4, 5]
        byte_array = bytearray(entiers)
        self.assertEqual(byte_array, bytearray(b'\x01\x02\x03\x04\x05'))

    def test_modification(self):
        entiers = [1, 2, 3, 4, 5]
        byte_array = bytearray(entiers)
        index = entiers.index(3)
        byte_array[index] = 10
        self.assertEqual(byte_array, bytearray(b'\x01\x02\n\x04\x05'))

    def test_main(self):
        if __name__ == '__main__':
            unittest.main()