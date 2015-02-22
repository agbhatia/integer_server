from integer_server.calculator.sequence_calculators import *
from integer_server.domain.sequence_domain import *

class SequenceService(object):
    """Responsible for retrieving the correct value from the corresponding calculator.
    Then it packages that value into a domain object which can be serialized.
    """

    def __init__(self, sequence_name):
        self.sequence_name = sequence_name
        self.calculator = CalculatorFactory().get_calculator(self.sequence_name)


    def get_nth_element(self, n):
        """Return the nth element of corresponding sequence
        :param n: int index of sequence to retrieve
        :return: SequenceElement obj that contains val at index n
        """
        val = self.calculator.get_nth_element(n)
        return SequenceElement(val, self.sequence_name)

    def get_sequence_list(self, n):
        """Return list of first n items in sequence
        :param n: int indicating num elements to return
        :return: list of first n elems in sequence
        """
        val = self.calculator.get_sequence_list(n)
        return SequenceList(val, self.sequence_name)

