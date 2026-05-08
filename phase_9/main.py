from repository import ItemRepository
from service import ItemService
from ui import TerminalUI


repo = ItemRepository()

service = ItemService(repo)

ui = TerminalUI(service)

ui.menu()