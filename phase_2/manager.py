from item import build_item

items = []
next_id = 1




def is_valid_title(title):
    return isinstance(title, str) and title.strip() != ""


def is_valid_id(id):
    return isinstance(id, int) and id > 0


def find_index(id):
    for i, item in enumerate(items):
        if item["id"] == id:
            return i
    return -1


def not_found():
    return None




def create_item(title, details):
    global next_id

    if not is_valid_title(title):
        return None

    item = build_item(next_id, title, details)
    items.append(item)
    next_id += 1
    return item


def list_items():
    return items


def find_item(id):
    if not is_valid_id(id):
        return None

    index = find_index(id)
    if index == -1:
        return not_found()

    return items[index]


def update_item(id, title, details):
    if not is_valid_id(id):
        return None

    index = find_index(id)
    if index == -1:
        return not_found()

    if title and is_valid_title(title):
        items[index]["title"] = title

    if details is not None:
        items[index]["details"] = details

    return items[index]


def delete_item(id):
    if not is_valid_id(id):
        return None

    index = find_index(id)
    if index == -1:
        return not_found()

    return items.pop(index)