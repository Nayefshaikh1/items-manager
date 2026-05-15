# api/errors.py

# Base API error
class APIError(Exception):

    def __init__(
        self,
        message,
        status=400
    ):

        super().__init__(message)

        self.message = message

        self.status = status


# Validation error
class ValidationError(APIError):

    def __init__(self, message):

        super().__init__(
            message,
            400
        )


# Authentication error
class AuthenticationError(APIError):

    def __init__(self, message):

        super().__init__(
            message,
            401
        )


# Not found error
class NotFoundError(APIError):

    def __init__(self, message):

        super().__init__(
            message,
            404
        )