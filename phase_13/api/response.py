# api/response.py

import json


# =========================
# SEND JSON RESPONSE
# =========================

def send_json(
    handler,
    payload,
    status=200
):

    # Status code
    handler.send_response(status)

    # JSON header
    handler.send_header(
        "Content-Type",
        "application/json"
    )

    # CORS support
    handler.send_header(
        "Access-Control-Allow-Origin",
        "*"
    )

    handler.send_header(
        "Access-Control-Allow-Headers",
        "*"
    )

    handler.send_header(
        "Access-Control-Allow-Methods",
        "GET, POST, PUT, DELETE, OPTIONS"
    )

    handler.end_headers()

    # Dict → JSON
    handler.wfile.write(
        json.dumps(payload).encode()
    )


# =========================
# SUCCESS RESPONSE
# =========================

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


# =========================
# ERROR RESPONSE
# =========================

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