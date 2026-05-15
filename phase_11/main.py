# main.py

from threading import Thread

from api.server import start_server

from ui import TerminalUI


# Start server in background
server_thread = Thread(

    target=start_server,

    daemon=True
)

server_thread.start()


# Start CLI
ui = TerminalUI()

ui.menu()