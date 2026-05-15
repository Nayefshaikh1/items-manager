# api/server.py

import os
import mimetypes

from http.server import (
    BaseHTTPRequestHandler,
    HTTPServer
)

from api.router import Router


# =========================
# WEB DIRECTORY
# =========================

WEB_DIR = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    ),
    "web"
)


# =========================
# API PATHS
# =========================

API_PATHS = [
    "/register",
    "/login",
    "/items",
    "/workflow"
]


def is_api_request(path):

    clean = path.split("?")[0]

    for api_path in API_PATHS:

        if clean == api_path:
            return True

        if clean.startswith(api_path + "/"):
            return True

    return False


# =========================
# STATIC FILE SERVING
# =========================

def serve_static(handler, path):

    # Default to index.html
    if path == "/":

        path = "/views/login.html"

    # Build file path
    file_path = os.path.join(
        WEB_DIR,
        path.lstrip("/")
    )

    # Normalize
    file_path = os.path.normpath(
        file_path
    )

    # Security check
    if not file_path.startswith(
        os.path.normpath(WEB_DIR)
    ):

        handler.send_response(403)
        handler.end_headers()
        return

    # File exists?
    if not os.path.isfile(file_path):

        handler.send_response(404)

        handler.send_header(
            "Content-Type",
            "text/html"
        )

        handler.end_headers()

        handler.wfile.write(
            b"<h1>404 Not Found</h1>"
        )

        return

    # Content type
    content_type, _ = mimetypes.guess_type(
        file_path
    )

    if not content_type:

        content_type = (
            "application/octet-stream"
        )

    # Read and serve
    with open(file_path, "rb") as f:

        content = f.read()

    handler.send_response(200)

    handler.send_header(
        "Content-Type",
        content_type
    )

    handler.send_header(
        "Content-Length",
        str(len(content))
    )

    handler.end_headers()

    handler.wfile.write(content)


# =========================
# REQUEST HANDLER
# =========================

class RequestHandler(
    BaseHTTPRequestHandler
):

    router = Router()

    # =========================
    # GET
    # =========================

    def do_GET(self):

        if is_api_request(self.path):

            self.router.handle(
                self,
                "GET"
            )

        else:

            serve_static(
                self,
                self.path.split("?")[0]
            )

    # =========================
    # POST
    # =========================

    def do_POST(self):

        self.router.handle(
            self,
            "POST"
        )

    # =========================
    # PUT
    # =========================

    def do_PUT(self):

        self.router.handle(
            self,
            "PUT"
        )

    # =========================
    # DELETE
    # =========================

    def do_DELETE(self):

        self.router.handle(
            self,
            "DELETE"
        )

    # =========================
    # OPTIONS
    # =========================

    def do_OPTIONS(self):

        self.send_response(200)

        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )

        self.send_header(
            "Access-Control-Allow-Headers",
            "*"
        )

        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, POST, PUT, DELETE, OPTIONS"
        )

        self.end_headers()

    # =========================
    # SUPPRESS LOGS
    # =========================

    def log_message(
        self,
        format,
        *args
    ):

        pass


# =========================
# START SERVER
# =========================

def start_server():

    server = HTTPServer(
        ("127.0.0.1", 8000),
        RequestHandler
    )

    print(
        "\nServer running at:\n"
        "http://127.0.0.1:8000\n"
    )

    server.serve_forever()