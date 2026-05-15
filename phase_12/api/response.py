# api/response.py

import json


def send_json(
    handler,
    payload,
    status=200
):

    # HTTP status
    handler.send_response(status)

    # JSON response type
    handler.send_header(
        "Content-Type",
        "application/json"
    )

    handler.end_headers()

    # Convert dict → JSON
    handler.wfile.write(
        json.dumps(payload).encode()
    )


# Success response
def success(
    handler,
    data,
    status=200
):

    payload = {
        "success": True,
        "data": data
    }

    send_json(
        handler,
        payload,
        status
    )


# Error response
def error(
    handler,
    message,
    status=400
):

    payload = {
        "success": False,
        "error": {
            "message": message
        }
    }

    send_json(
        handler,
        payload,
        status
    )