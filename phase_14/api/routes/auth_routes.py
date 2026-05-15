# api/routes/auth_routes.py

from app_context import (
    service,
    auth
)

from api.request_parser import parse_json

from api.response import (
    success,
    error
)


# POST /register
def register(handler):

    try:

        data = parse_json(handler)

        service.register(
            data["username"],
            data["password"],
            data.get("role", "user")
        )

        success(
            handler,
            {
                "message": "registered"
            },
            201
        )

    except Exception as e:

        error(handler, str(e))


# POST /login
def login(handler):

    try:

        data = parse_json(handler)

        token = service.login(
            data["username"],
            data["password"]
        )

        success(
            handler,
            {
                "token": token
            }
        )

    except Exception as e:

        error(handler, str(e), 401)