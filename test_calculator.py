import unittest

import calculator
from calculator import *

class TestCalculator(unittest.TestCase):
   # Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_mul(self): # 3 assertions
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(0, 9), 0)
        self.assertEqual(calculator.mul(-8, 4), -32)
    def test_div(self): # 3 assertions
        self.assertEqual(calculator.div(2,4 ), 2)
        self.assertEqual(calculator.div(8,-64 ), -8)
        self.assertEqual(calculator.div(2,32), 16)

        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 49)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 23)
        with self.assertRaises(ValueError):
            calculator.logarithm(-4, 9)
    #

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(calculator.hypotenuse(12, 5), 13)
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)


    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        self.assertAlmostEqual(calculator.square_root(64), 8.0)
        self.assertAlmostEqual(calculator.square_root(144), 12.0)
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            calculator.square_root(-6)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()