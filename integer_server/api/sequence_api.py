from integer_server import app
from flask import jsonify
from integer_server.validators import validate_sequence
from integer_server.services.sequence_services import SequenceService

@app.route('/sequences/<string:sequence_name>/<int:element_number>')
@validate_sequence
def get_element_in_sequence(sequence_name, element_number):
    """Route for retrieving nth element in given sequence
    :param sequence_name: string of sequence name
    :param element_number: int index to retrieve in sequence name
    :return: json of element at nth index of seq
    """
    element = SequenceService(sequence_name).get_nth_element(element_number)
    return jsonify(element.to_dict())

@app.route('/sequences/<string:sequence_name>/first/<int:element_number>')
@validate_sequence
def get_sequence(sequence_name, element_number):
    """Route for retrieving first n elements in sequence
    :param sequence_name: string
    :param element_number: int indicating num of elements to return
    :return: json of list of first n elements
    """
    element = SequenceService(sequence_name).get_sequence_list(element_number)
    return jsonify(element.to_dict())

