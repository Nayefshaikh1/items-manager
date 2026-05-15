# main.py

import time

from threading import Thread

from ui import TerminalUI

from api.server import start_server

from app_context import service


# ---------- START SERVER ----------

def run_server():

    try:

        start_server()

    except Exception as e:

        print(
            f"Server Error: {e}"
        )


server_thread = Thread(

    target=run_server,

    daemon=True
)

server_thread.start()

# Wait for server startup
time.sleep(2)

print(
    "\nAPI SERVER STARTED\n"
)

print(
    "Open browser:\n"
    "http://127.0.0.1:8000/\n"
)

# ---------- START CLI ----------

ui = TerminalUI(service)

ui.menu()