from items_manager import ItemsManager


def run_tests():
    manager = ItemsManager()

    # CREATE
    item1 = manager.create_item("Task1", "Details1")
    assert item1.id == 1

    # MULTIPLE
    manager.create_item("Task2", "Details2")
    assert len(manager.list_items()) == 2

    # FIND
    found = manager.find_item(1)
    assert found.title == "Task1"

    # UPDATE
    updated = manager.update_item(1, "Updated", None)
    assert updated.title == "Updated"

    # DELETE
    deleted = manager.delete_item(2)
    assert deleted.id == 2
    assert len(manager.list_items()) == 1

    print("Phase 1 tests passed")


if __name__ == "__main__":
    run_tests()