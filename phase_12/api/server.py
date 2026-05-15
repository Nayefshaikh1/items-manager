# api/server.py

from http.server import (
    BaseHTTPRequestHandler,
    HTTPServer
)

from api.router import Router


class RequestHandler(
    BaseHTTPRequestHandler
):

    router = Router()

    # GET
    def do_GET(self):

        self.router.handle(
            self,
            "GET"
        )

    # POST
    def do_POST(self):

        self.router.handle(
            self,
            "POST"
        )

    # PUT
    def do_PUT(self):

        self.router.handle(
            self,
            "PUT"
        )

    # DELETE
    def do_DELETE(self):

        self.router.handle(
            self,
            "DELETE"
        )


def start_server():

    server = HTTPServer(

        ("127.0.0.1", 8000),

        RequestHandler
    )

    print(
        "Server running at:\n"
        "http://127.0.0.1:8000"
    )

    server.serve_forever()