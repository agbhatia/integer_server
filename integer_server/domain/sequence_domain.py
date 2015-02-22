# Domain objects are responsible for containing data and knowing how to serialize themselves

class BaseDomain(object):
    """Base class for domain objects"""

    def to_dict(self):
        raise NotImplementedError()

class SequenceElement(BaseDomain):
    """Represents one value of sequence. Used for returning nth element"""
    def __init__(self, value, sequence_type):
        super(SequenceElement, self).__init__()
        self.value = value
        self.sequence_type = sequence_type

    def to_dict(self):
        """
        :return: dict representation of self
        """
        return {
            "type": "sequence_element",
            "sequence": self.sequence_type,
            "value": self.value
        }

class SequenceList(BaseDomain):
    """Represents list of values in a sequence. Used for returning first n elems of seq."""

    def __init__(self, values, sequence_type):
        super(SequenceList, self).__init__()
        self.values = values
        self.sequence_type = sequence_type

    def to_dict(self):
        """
        :return: dict representation of self
        """
        return {
            "type": "sequence_list",
            "sequence": self.sequence_type,
            "values": self.values
        }