class ResourceException(Exception):
    code = None
    http_status = None

    def __init__(self):
        self.message = None

    def to_dict(self):
        return {"message": self.message, "code": self.code}

class InvalidSequenceException(ResourceException):
    code = "invalid_sequence"
    http_status = 400

    def __init__(self, sequence_name):
        super(InvalidSequenceException, self).__init__()
        self.message = "Invalid sequence: %s" % sequence_name


class InvalidElementException(ResourceException):
    code = "invalid_element"
    http_status = 403

    def __init__(self, element_num):
        super(InvalidElementException, self).__init__()
        self.message = "Invalid element num: %s" % str(element_num)

