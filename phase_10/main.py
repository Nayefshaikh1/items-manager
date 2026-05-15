from repository import Repository
from auth import AuthManager
from service import ItemService
from ui import TerminalUI


repo = Repository()

auth = AuthManager()

service = ItemService(
    repo,
    auth
)

ui = TerminalUI(service)

ui.menu()