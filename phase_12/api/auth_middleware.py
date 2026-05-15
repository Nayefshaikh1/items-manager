# api/auth_middleware.py


def extract_token(handler):

    auth_header = handler.headers.get(
        "Authorization"
    )

    # Missing header
    if not auth_header:

        raise PermissionError(
            "Authorization header missing"
        )

    parts = auth_header.split()

    # Must be:
    # Bearer <token>
    if (
        len(parts) != 2
        or parts[0] != "Bearer"
    ):

        raise PermissionError(
            "Invalid authorization header"
        )

    # Return token only
    return parts[1]