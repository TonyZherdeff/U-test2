import unittest
from main import Number


class NumberTest(unittest.TestCase):
    def setUp(self):
        self.num = Number(10)

    def test_read(self):
        self.assertEqual(self.num.read_num(), 10)
        self.assertEqual(self.num.read_num(), "10")

    def test_write(self):
        self.assertEqual(self.num.write_num(11), 11)
        self.assertEqual(self.num.write_num(11), 5)

    def test_oct(self):
        self.assertEqual(self.num.oct_num(), "12")
        self.assertEqual(self.num.oct_num(), 8.11)

    def test_hex(self):
        self.assertEqual(self.num.hex_num(), "a")
        self.assertEqual(self.num.hex_num(), 10)

    def test_bin(self):
        self.assertEqual(self.num.bin_num(), "1010")
        self.assertEqual(self.num.bin_num(), 1010)


if __name__ == '__main__':
    unittest.main()