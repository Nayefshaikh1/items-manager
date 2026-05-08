from postgres_repository import PostgresRepository
from item_service import ItemService


def display(items):

    for item in items:
        print(item)


def main():

    repo = PostgresRepository()

    service = ItemService(repo)

    # CREATE
    item1 = service.create_item(
        "Learn PostgreSQL",
        "Docker setup"
    )

    item2 = service.create_item(
        "Build API",
        "FastAPI later"
    )

    print("\n--- ALL ITEMS ---")
    display(service.list_items())

    # FIND
    print("\n--- FIND ITEM ---")
    print(service.find_item(item1.id))

    # UPDATE
    service.update_item(
        item1.id,
        title="Learn PostgreSQL Deeply"
    )

    print("\n--- AFTER UPDATE ---")
    print(service.find_item(item1.id))

    # DELETE
    service.delete_item(item2.id)

    print("\n--- FINAL ITEMS ---")
    display(service.list_items())


if __name__ == "__main__":
    main()