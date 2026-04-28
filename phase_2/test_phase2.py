from manager import *

def run_tests():

    # CREATE
    item1 = create_item("Task1", "Details1")
    assert item1["id"] == 1

    # INVALID CREATE
    assert create_item("", "X") is None

    # MULTIPLE
    create_item("Task2", "D2")
    create_item("Task3", "D3")
    assert len(list_items()) == 3

    # FIND
    assert find_item(1)["title"] == "Task1"
    assert find_item(99) is None

    # UPDATE
    updated = update_item(1, "Updated", None)
    assert updated["title"] == "Updated"

    # DELETE
    deleted = delete_item(2)
    assert deleted["id"] == 2

    # INVALID DELETE
    assert delete_item(99) is None

    print("All tests passed")


if __name__ == "__main__":
    run_tests()