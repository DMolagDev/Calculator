import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_sum(self):
        calculator = Calculator(10, 2)
        self.assertEqual(calculator.sum(), 12)

    def test_subtract(self):
        calculator = Calculator(10, 2)
        self.assertEqual(calculator.subtract(), 8)

    def test_multiply(self):
        calculator = Calculator(10, 2)
        self.assertEqual(calculator.multiply(), 20)

    def test_divide(self):
        calculator = Calculator(10, 2)
        self.assertEqual(calculator.divide(), 5)

    def test_divide_by_zero(self):
            calculator = Calculator(10, 0)

            with self.assertRaises(ValueError):
                calculator.divide()


if __name__ == "__main__":
    unittest.main()