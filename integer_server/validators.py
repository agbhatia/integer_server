from integer_server.exceptions import InvalidSequenceException
from functools import wraps
from integer_server import constants as c

# set of valid sequences.
# use a set to make lookup constant time
valid_sequences = {c.FIB_SEQ, c.HAPPY_NUM_SEQ}

# Function to check if sequence is valid
# create own function in case other parts of code might want to use this
def is_valid_sequence(sequence_name):
    return sequence_name in valid_sequences

# decorator to determine if the sequence name is valid
# raise an exception if not
def validate_sequence(f):
    @wraps(f)
    def decorated_function(sequence_name, *args, **kwargs):
        if not is_valid_sequence(sequence_name):
            raise InvalidSequenceException(sequence_name)
        else:
            return f(sequence_name, *args, **kwargs)
    return decorated_function