from storage import JsonStorage
from file_repository import FileItemRepository
from item_service import ItemService

def display(items):
    for item in items:
        print(item)

def main():
    # Composition root
    storage = JsonStorage("data.json")
    repository = FileItemRepository(storage)
    service = ItemService(repository)

    service.create_item("Task1", "Details1")
    service.create_item("Task2", "Details2")

    print("\nAll items:")
    display(service.list_items())

    service.update_item(1, title="Updated Task")

    print("\nAfter update:")
    display(service.list_items())

    service.delete_item(2)

    print("\nFinal:")
    display(service.list_items())

if __name__ == "__main__":
    main()