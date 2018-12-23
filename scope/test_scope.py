import unittest
from scope.class_main import Sub0, Sub1


class GlobalValTester(unittest.TestCase):
    def test_01_Sub1(self):
        self.assertEqual(Sub1().value, 1)

    def test_02_Sub0(self):
        self.assertIsNot(Sub0(), 1)

    def test_03_Sub1(self):
        self.assertEqual(Sub1().value, 1)

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
