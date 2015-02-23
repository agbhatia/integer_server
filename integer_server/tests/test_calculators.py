import unittest

from integer_server.calculator.sequence_calculators import FibonacciCalculator, HappyNumberCalculator
from integer_server.exceptions import InvalidElementException


class FibonacciCalculatorTest(unittest.TestCase):
    def setUp(self):
        """Define a list of the known fib sequence up to a certain point. This should be
        good enough to test that it works (can make the list longer if needed).
        """
        self.fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
        self.calculator = FibonacciCalculator()

    def test_fib_calculator_elements(self):
        """Test the get nth element fib calculation for all the indices in the setup list"""
        calc_result = [self.calculator.get_nth_element(i) for i in xrange(len(self.fib))]
        self.assertEqual(calc_result, self.fib)

    def test_fib_calculator_list(self):
        """Test the list generation function in the fib calc"""
        for i in xrange(len(self.fib)+1):
            calc_result = self.calculator.get_sequence_list(i)
            expected_result = self.fib[:i]
            self.assertEqual(calc_result, expected_result)

class HappyNumberTest(unittest.TestCase):
    def setUp(self):
        """Define a list of the known happy numbers seq up to a certain point. This should
        ""be good enough to test that it works (can make the list longer if needed).
        """
        self.happy_numbers = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190]
        self.calculator = HappyNumberCalculator()

    def test_happy_number_calculator_element_zero(self):
        """Test that happy_number(0) raises an exception"""
        with self.assertRaises(InvalidElementException):
            self.calculator.get_nth_element(0)

    def test_happy_number_calculator_elements(self):
        """Test the get nth element happy number calc for all the indices in the setup list"""

        # Start at index 1 since happy_number(0) throws an exception
        calc_result = [self.calculator.get_nth_element(i) for i in xrange(1, len(self.happy_numbers)+1)]
        self.assertEqual(calc_result, self.happy_numbers)

    def test_happy_number_calculator_list(self):
        """Test the list generation function in the happy num calculator"""
        for i in xrange(len(self.happy_numbers)+1):
            calc_result = self.calculator.get_sequence_list(i)
            expected_result = self.happy_numbers[:i]
            self.assertEqual(calc_result, expected_result)


if __name__ == "__main__":
    unittest.main()