# api/request_parser.py

import json


def parse_json(handler):

    # Read content length
    content_length = int(
        handler.headers.get(
            "Content-Length",
            0
        )
    )

    # Empty body
    if content_length == 0:

        return {}

    # Read request body
    body = handler.rfile.read(
        content_length
    )

    # Convert JSON → Python dict
    return json.loads(body)