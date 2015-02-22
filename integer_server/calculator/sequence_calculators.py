from integer_server.exceptions import *
from integer_server import constants as c

class CalculatorFactory(object):
    """Takes in the sequence name and spits out the corresponding calculator"""

    def get_calculator(self, sequence_name):
        """
        :param sequence_name: string of the sequence name
        :return: BaseCalculator obj that corresponds to sequence name
        """
        if (sequence_name == c.FIB_SEQ):
            return FibonacciCalculator()
        elif (sequence_name == c.HAPPY_NUM_SEQ):
            return HappyNumberCalculator()
        else:
            # This case shouldn't really be hit since we validate the sequence
            # name when the api immediately gets hit. But we just put this here
            # for completeness of the if else case.
            raise InvalidSequenceException(sequence_name)

class BaseCalculator(object):
    """This is the base class meant to serve as a blueprint for the fib and happy num
    calculators. Raise Not implemented errors for functions that must be defined
    in the subclasses. Also meant to define common functions that can be used
    across all its subclasses.
    """

    def get_nth_element(self, n):
        raise NotImplementedError()

    def get_sequence_list(self, n):
        raise NotImplementedError()

    def get_last_elem_from_generator(self, generator):
        # Initialize last in case there are no elements in the generator
        last = None
        for last in generator:
            pass
        return last


class FibonacciCalculator(BaseCalculator):
    """Class to handle fib calculations"""

    def fib_generator(self, n):
        """Iteratively generate fibonacci sequence up to n
        :param n: int index of element to retrieve up to
        """
        if (n < 0):
            return

        (x, y) = (0, 1)

        yield x

        for i in xrange(n):
            (x, y) = (y, x+y)
            yield x

    def get_nth_element(self, n):
        """Retrieve nth element of fib sequence
        :param n: int index of element to retrieve
        :return: int value of element
        :raises InvalidElementException: if n is an invalid index (< 0)
        """
        if (n < 0):
            raise InvalidElementException(n)
        # We simply need to get the last element of the generator
        return self.get_last_elem_from_generator(self.fib_generator(n))


    def get_sequence_list(self, n):
        """Calculate first n elements in fib sequence
        :param n: int indicating how many elements to return
        :return: list of first n elements in fib sequence
        """
        return [i for i in self.fib_generator(n-1)]

class HappyNumberCalculator(BaseCalculator):
    """Class to handle happy number calculations"""
    def __init__(self):
        # We keep a reference to the squares of all the numbers from 0-9
        # because we only square each digit. Saves time from constantly
        # calculating the squares.
        self.squared_dict = {i:i**2 for i in xrange(10)}

        # We memoize all the unhappy and happy numbers so we aren't performing duplicate
        # calculations. There is a significant time improvement with this method (I profiled
        # the times). Memoizing does increase performance at the cost of using up more memory,
        # but the amount of extra consumed isn't very expensive.
        self.happy_number_set = set()
        self.unhappy_number_set = set()

    def is_happy_helper(self, n):
        """ This function does 2 important things. 1: determines if n is a happy number or not
        2: It capture the set of values that led to the result so we can memoize those numbers
        to greatly speed up future calculations.
        :param n: int of value we are checking
        :return (bool, set): bool to indicate if n is happy, and set to capture all the values that led to the result
        """
        previous_values = set()

        while (n > 1) and (n not in previous_values):
            # First check if n is in the happy or unhappy number set or not. If it is in one
            # of the lists then we immediately know if n is happy or not.
            if n in self.happy_number_set:
                return (True, previous_values)
            elif n in self.unhappy_number_set:
                return (False, previous_values)

            previous_values.add(n)
            n = sum([self.squared_dict[int(ch)] for ch in str(n)])

        return (n == 1, previous_values)

    def happy_number_generator(self, n):
        """Generator to return the next happy number
        :param n: int of index to generate up to
        :return: next happy number
        """
        if (n < 1):
            return
        i = 0
        count = 0

        # It is important to track the values returned by the helper function
        # so that we can leverage them to speed up future calculations.
        while (count < n):
            i += 1
            (is_happy, value_set) = self.is_happy_helper(i)
            if (is_happy):
                count += 1
                yield i
                # Add the value set into our list of happy numbers
                self.happy_number_set |= value_set
            else:
                # Add the value set into our list of unhappy numbers
                self.unhappy_number_set |= value_set

    def get_nth_element(self, n):
        """Return nth element of happy num sequence
        :param n: int index of element to return
        :return: int value of element
        :raises InvalidElementException: if n is an invalid index (< 1)
        """
        if (n < 1):
            raise InvalidElementException(n)
        # We simply need to get the last element of the generator
        return self.get_last_elem_from_generator(self.happy_number_generator(n))

    def get_sequence_list(self, n):
        """Return list of first n elements
        :param n: int indicating num of elements to return up to
        :return: list of first n elements
        """
        return [i for i in self.happy_number_generator(n)]
