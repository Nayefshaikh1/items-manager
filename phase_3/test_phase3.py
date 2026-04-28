from manager import ItemsManager

def run_tests():
    manager = ItemsManager()

    # CREATE
   
    item1 = manager.create_item("A", "D1")
    
    assert item1 is not None

    # LIST
    assert len(manager.list_items()) >= 1

    # FIND
    found = manager.find_item(item1["id"])
    assert found is not None

    # UPDATE
    updated = manager.update_item(item1["id"], "Updated", None)
    assert updated["title"] == "Updated"

    # DELETE
    deleted = manager.delete_item(item1["id"])
    assert deleted is not None

    print("Phase 3 tests passed")

if __name__ == "__main__":
    run_tests()