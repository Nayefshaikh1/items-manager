# api/routes/item_routes.py

from urllib.parse import (
    urlparse,
    parse_qs
)

from app_context import (
    service,
    auth
)

from api.request_parser import parse_json

from api.response import (
    success,
    error
)

from api.validation import (
    validate_item_payload
)

from api.auth_middleware import (
    extract_token
)


# ---------- CREATE ITEM ----------

# POST /items
def create_item(handler):

    try:

        # Extract token
        token = extract_token(handler)

        # Authenticate user
        auth.authenticate_token(token)

        # Parse JSON body
        data = parse_json(handler)

        # Validate request
        validate_item_payload(data)

        # Create item
        item = service.create_item(
            data["title"],
            data.get("details", "")
        )

        # Success response
        success(
            handler,
            {
                "id": item.id,
                "title": item.title,
                "details": item.details,
                "state": item.state
            },
            201
        )

    except Exception as e:

        error(handler, str(e))


# ---------- GET SINGLE ITEM ----------

# GET /items/1
def get_item(
    handler,
    item_id
):

    try:

        token = extract_token(handler)

        auth.authenticate_token(token)

        item = service.get_item(
            item_id
        )

        success(
            handler,
            {
                "id": item.id,
                "title": item.title,
                "details": item.details,
                "state": item.state
            }
        )

    except Exception as e:

        error(handler, str(e), 404)


# ---------- GET ALL ITEMS ----------

# GET /items
# GET /items?state=active
def get_all_items(handler):

    try:

        token = extract_token(handler)

        auth.authenticate_token(token)

        # Parse query parameters
        parsed = urlparse(handler.path)

        query = parse_qs(parsed.query)

        # Filter by state
        if "state" in query:

            items = (
                service.get_items_by_state(
                    query["state"][0]
                )
            )

        else:

            items = (
                service.get_all_items()
            )

        result = []

        for item in items:

            result.append({

                "id": item.id,

                "title": item.title,

                "details": item.details,

                "state": item.state
            })

        success(
            handler,
            result
        )

    except Exception as e:

        error(handler, str(e))


# ---------- UPDATE ITEM ----------

# PUT /items/1
def update_item(
    handler,
    item_id
):

    try:

        token = extract_token(handler)

        auth.authenticate_token(token)

        data = parse_json(handler)

        item = service.update_item(
            item_id,
            data["title"],
            data["details"]
        )

        success(
            handler,
            {
                "message": "updated",
                "id": item.id
            }
        )

    except Exception as e:

        error(handler, str(e))


# ---------- DELETE ITEM ----------

# DELETE /items/1
def delete_item(
    handler,
    item_id
):

    try:

        token = extract_token(handler)

        auth.authenticate_token(token)

        service.delete_item(
            item_id
        )

        success(
            handler,
            {
                "message": "deleted"
            }
        )

    except Exception as e:

        error(handler, str(e))