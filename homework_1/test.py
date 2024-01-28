import unittest
from .Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()
        self.a = 5
        self.b = 2

    def test_adding(self):
        self.assertEqual(self.calc.add(self.a, self.b), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(self.a, self.b), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(self.a, self.b), 10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(self.a, self.b), 2)

    def test_subtract_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, 4, 0)

    def test_calculate_discount(self):
        self.assertEqual(self.calc.calculate_discount(100, 20), 80)

    def test_calculate_discount_not_number(self):
        self.assertRaises(AssertionError, self.calc.calculate_discount, 100, '20')

    def test_calculate_discount_negative_discount(self):
        self.assertRaises(AssertionError, self.calc.calculate_discount, 100, -20)

    def test_calculate_discount_greater_100_discount(self):
        self.assertRaises(AssertionError, self.calc.calculate_discount, 100, 120)


if __name__ == '__main__':
    unittest.main()
