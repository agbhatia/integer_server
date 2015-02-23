"""Initialize the app"""

from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions, HTTPException
from integer_server.exceptions import ResourceException

def make_json_app(import_name, **kwargs):
    """This function initializes the app."""

    def make_json_error(ex):
        """This is an error handler for handling exceptions for the app. It allows
        us to simply handle all the exceptions here as opposed to writing try catches
        everywhere. The ResourceExceptions defined in the app will be serialized
        accordingly.
        """
        if isinstance(ex, HTTPException):
            return ex;
        elif isinstance(ex, ResourceException):
            info = ex.to_dict()
            status_code = ex.http_status
            info["type"] = "exception"
        else:
            message = "There was an internal server error. Please try again later."
            info = {"code": "internal_server_error", "message": message, "type": "exception"}
            status_code = 500
            # generally we should log these 500 errors with the stacktrace somewhere -- we used splunk at Box.

        response = jsonify(**info)
        response.status_code = status_code
        return response

    app = Flask(import_name, **kwargs)

    # loop through all the error http status codes and register our
    # error callback to handle them.
    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error

    return app

app = make_json_app(__name__)