# app_context.py

from repository import Repository

from auth import AuthManager

from service import ItemService


repo = Repository()

auth = AuthManager()

service = ItemService(
    repo,
    auth
)