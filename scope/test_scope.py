import unittest
from scope.class_main import Sub0, Sub1


class GlobalValTester(unittest.TestCase):
    def test_01_Sub1(self):
        self.assertEqual(Sub1().value, 1)

    def test_02_Sub0(self):
        self.assertIsNot(Sub0(), 1)

    def test_03_Sub1(self):
        self.assertEqual(Sub1().value, 1)
        self.assertEqual(Sub1().value_self, 'this is class value 1')
        Sub1.inc_cls_val()
        self.assertEqual(Sub1.get_value_classmethod(), 'this is class value 2')

    def test_04_Sub1_staticm(self):
        Sub1.inc_val()
        Sub1.inc_val()
        Sub1.inc_val()
        self.assertEqual(Sub1.get_value_staticmethod(), 4)

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
