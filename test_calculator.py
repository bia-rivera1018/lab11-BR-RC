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

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)

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
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()