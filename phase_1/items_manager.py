class Item:
    def __init__(self, id, title, details):
        self.id = id
        self.title = title
        self.details = details

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Details: {self.details}"


class ItemsManager:
    def __init__(self):
        self.items = []
        self.next_id = 1

    # CREATE
    def create_item(self, title, details):
        if not title:
            return None

        item = Item(self.next_id, title, details)
        self.items.append(item)
        self.next_id += 1
        return item

    # LIST
    def list_items(self):
        return self.items

    # FIND
    def find_item(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None

    # UPDATE
    def update_item(self, id, title, details):
        item = self.find_item(id)
        if not item:
            return None

        if title:
            item.title = title
        if details:
            item.details = details

        return item

    # DELETE
    def delete_item(self, id):
        for i, item in enumerate(self.items):
            if item.id == id:
                return self.items.pop(i)
        return None


# TEST RUN (optional)
if __name__ == "__main__":
    manager = ItemsManager()

    manager.create_item("Task1", "Details1")
    manager.create_item("Task2", "Details2")

    for item in manager.list_items():
        print(item)