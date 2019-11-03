from flask import make_response, jsonify

from .http_enums import HttpStatusCode, HTTPResponseMessage


class HTTPResponse:
    """ HTTP Response helper class """

    @staticmethod
    def _build_error_response(message, status_code, error_id, **kwargs):
        """ Builds an error HTTP response object (Flask.Response) to return to the client """

        return make_response(
            jsonify({
                "status_code": status_code,
                "error": {
                    "message": message,
                    "id": error_id
                },
                **kwargs
            }), status_code
        )

    @staticmethod
    def _build_response(message, status_code, data=None, **kwargs):
        """ Builds a successful HTTP response object (Flask.Response) to return to the client """

        return make_response(
            jsonify({
                "message": message,
                "status_code": status_code,
                "data": [] if not data else data,
                **kwargs
            }), status_code
        )

    def _build_obj_response(message, status_code, data=None, **kwargs):
        """ Builds a successful HTTP response object (Flask.Response) to return to the client """

        return make_response(
            {
                "message": message,
                "status_code": status_code,
                "data": data,
                **kwargs
            } , status_code,
        )
    @staticmethod
    def ok(message=None, data=None, **kwargs):
        """ Returns an HTTP Response (200 OK)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            data (list): A Python list in a JSON serializable format
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_response(
            message=HTTPResponseMessage.OK.value if not message else message,
            status_code=HttpStatusCode.OK.value,
            data=[] if not data else data,
            **kwargs
        )

    @staticmethod
    def created(message=None, data=None, **kwargs):
        """ Returns an HTTP Response (201 Created)


        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            data (list): A Python list in a JSON serializable format
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_response(
            message=HTTPResponseMessage.CREATED.value if not message else message,
            status_code=HttpStatusCode.CREATED.value,
            data=[] if not data else data,
            **kwargs
        )

    @staticmethod
    def accepted(message=None, data=None, **kwargs):
        """ Returns an HTTP Response (202 accepted)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            data (list): A Python list in a JSON serializable format
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_response(
            message=HTTPResponseMessage.ACCEPTED.value if not message else message,
            status_code=HttpStatusCode.ACCEPTED.value,
            data=[] if not data else data,
            **kwargs
        )


    @staticmethod
    def accepted_req(message=None, data=None, **kwargs):
        """ Returns an HTTP Response (202 accepted)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            data (list): A Python list in a JSON serializable format
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_obj_response(
            message=HTTPResponseMessage.ACCEPTED.value if not message else message,
            status_code=HttpStatusCode.ACCEPTED.value,
            data=[] if not data else data,
            **kwargs
        )

    @staticmethod
    def no_content(message=None, data=None, **kwargs):
        """ Returns an HTTP Response (204 no content)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            data (list): A Python list in a JSON serializable format
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_response(
            message=HTTPResponseMessage.NO_CONTENT.value if not message else message,
            status_code=HttpStatusCode.NO_CONTENT.value,
            data=[] if not data else data,
            **kwargs
        )

    @staticmethod
    def moved_permanently(message=None, data=None, **kwargs):
        """ Returns an HTTP Response (301 Moved Permanently)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            data (list): A Python list in a JSON serializable format
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_response(
            message=HTTPResponseMessage.MOVED_PERMANENTLY.value if not message else message,
            status_code=HttpStatusCode.MOVED_PERMANENTLY.value,
            data=[] if not data else data,
            **kwargs
        )

    @staticmethod
    def bad_request(message=None, error_id=None, **kwargs):
        """ Returns an HTTP Response (400 Bad Request)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            error_id (str): An error id that should be logged before calling this method (for easy tracing of the error)
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_error_response(
            message=HTTPResponseMessage.BAD_REQUEST.value if not message else message,
            status_code=HttpStatusCode.BAD_REQUEST.value,
            error_id=error_id,
            **kwargs
        )

    @staticmethod
    def unauthorized(message=None, error_id=None, **kwargs):
        """ Returns an HTTP Response (401 Unauthorized)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            error_id (str): An error id that should be logged before calling this method (for easy tracing of the error)
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_error_response(
            message=HTTPResponseMessage.UNAUTHORIZED.value if not message else message,
            status_code=HttpStatusCode.UNAUTHORIZED.value,
            error_id=error_id,
            **kwargs
        )

    @staticmethod
    def forbidden(message=None, error_id=None, **kwargs):
        """ Returns an HTTP Response (403 Forbidden)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            error_id (str): An error id that should be logged before calling this method (for easy tracing of the error)
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_error_response(
            message=HTTPResponseMessage.FORBIDDEN.value if not message else message,
            status_code=HttpStatusCode.FORBIDDEN.value,
            error_id=error_id,
            **kwargs
        )

    @staticmethod
    def not_found(message=None, error_id=None, **kwargs):
        """ Returns an HTTP Response (404 Not Found)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            error_id (str): An error id that should be logged before calling this method (for easy tracing of the error)
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_error_response(
            message=HTTPResponseMessage.NOT_FOUND.value if not message else message,
            status_code=HttpStatusCode.NOT_FOUND.value,
            error_id=error_id,
            **kwargs
        )

    @staticmethod
    def method_not_allowed(message=None, error_id=None, **kwargs):
        """ Returns an HTTP Response (405 Method Not Allowed)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            error_id (str): An error id that should be logged before calling this method (for easy tracing of the error)
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_error_response(
            message=HTTPResponseMessage.METHOD_NOT_ALLOWED.value if not message else message,
            status_code=HttpStatusCode.METHOD_NOT_ALLOWED.value,
            error_id=error_id,
            **kwargs
        )

    @staticmethod
    def internal_server_error(message=None, error_id=None, **kwargs):
        """ Returns an HTTP Response (500 Internal Server Error)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            error_id (str): An error id that should be logged before calling this method (for easy tracing of the error)
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_error_response(
            message=HTTPResponseMessage.INTERNAL_SERVER_ERROR.value if not message else message,
            status_code=HttpStatusCode.INTERNAL_SERVER_ERROR.value,
            error_id=error_id,
            **kwargs
        )

    @staticmethod
    def not_implemented(message=None, error_id=None, **kwargs):
        """ Returns an HTTP Response (501 Not Implemented)

        Args:
            message (str): A message to return to the client (Defaults to the corresponding HTTPStatusMessage)
            error_id (str): An error id that should be logged before calling this method (for easy tracing of the error)
            **kwargs: Any kwargs to be added to the object
        Returns:
            A Flask response object (flask.Response)
        """

        return HTTPResponse._build_error_response(
            message=HTTPResponseMessage.NOT_IMPLEMENTED.value if not message else message,
            status_code=HttpStatusCode.NOT_IMPLEMENTED.value,
            error_id=error_id,
            **kwargs
        )

