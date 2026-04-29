from item_store import ItemStore
from item_service import ItemService
from storage import JsonStorage

def display_items(items):
    if not items:
        print("No items available")
        return

    for item in items:
        print(item)

def main():
    # Composition root
    storage = JsonStorage("data.json")
    store = ItemStore(storage)
    service = ItemService(store)

    # Demo flow
    service.create_item("Learn Python", "Basics")
    service.create_item("Practice DSA", "Daily")

    print("\nAll items:")
    display_items(service.list_items())

    print("\nUpdate item 1:")
    service.update_item(1, title="Learn Python Deeply")

    print("\nAfter update:")
    display_items(service.list_items())

    print("\nDelete item 2:")
    service.delete_item(2)

    print("\nFinal items:")
    display_items(service.list_items())

if __name__ == "__main__":
    main()