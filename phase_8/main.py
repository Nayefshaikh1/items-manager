from repository import ItemRepository
from service import ItemService


repo = ItemRepository()

service = ItemService(repo)

item = service.create_item(
    "Learn Workflow",
    "Phase 8"
)

print(item)

service.transition_item(
    item.id,
    "active"
)

service.transition_item(
    item.id,
    "completed"
)

print("\nSUMMARY:")
print(service.workflow_summary())

print("\nCOMPLETED ITEMS:")
print(service.filter_items("completed"))

print("\nHISTORY:")
print(repo.get_history(item.id))