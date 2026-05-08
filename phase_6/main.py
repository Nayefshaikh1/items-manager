from storage import JsonStorage
from file_repository import FileRepository
from item_service import ItemService

def main():
    storage = JsonStorage()
    repo = FileRepository(storage)
    service = ItemService(repo)

    item = service.create_item("Task", "Details")
    print(item)

    service.update_item(item.id, title="Updated Task")
    print(service.find_item(item.id))

if __name__ == "__main__":
    main()