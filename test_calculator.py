# https://github.com/bia-rivera1018/lab11-BR-RC.git
# Partner 1: Bianca Rivera
# Partner 2: Rodrigo Cardenas

import math
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0

    def test_subtract(self):
        assert calculator.subtract(5, 2) == 3
        assert calculator.subtract(2, 5) == -3
        assert calculator.subtract(0, 0) == 0

    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(0, 9), 0)
        self.assertEqual(calculator.mul(-8, 4), -32)

    def test_divide(self):
        self.assertEqual(calculator.div(2,4 ), 2)
        self.assertEqual(calculator.div(8,-64 ), -8)
        self.assertEqual(calculator.div(2,32), 16)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        result = calculator.logarithm(10, 100)
        assert math.isclose(result, 2.0, rel_tol=1e-9)

        result = calculator.logarithm(2, 8)
        assert math.isclose(result, 3.0, rel_tol=1e-9)

        result = calculator.logarithm(math.e, math.e ** 5)
        assert math.isclose(result, 5.0, rel_tol=1e-9)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(4, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(12, 5), 13)
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        self.assertAlmostEqual(calculator.square_root(64), 8.0)
        self.assertAlmostEqual(calculator.square_root(144), 12.0)

        with self.assertRaises(ValueError):
            calculator.square_root(-6)

if __name__ == "__main__":
    unittest.main()