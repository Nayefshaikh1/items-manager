# api/routes/item_routes.py

from urllib.parse import (
    urlparse,
    parse_qs
)

from app_context import (
    service,
    auth
)

from api.request_parser import (
    parse_json
)

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


# =========================
# CREATE ITEM
# POST /items
# =========================

def create_item(handler):

    try:

        # Token
        token = extract_token(
            handler
        )

        auth.authenticate_token(
            token
        )

        # Parse body
        data = parse_json(
            handler
        )

        # Validate
        validate_item_payload(
            data
        )

        # Create
        item = service.create_item(

            data["title"],

            data.get(
                "details",
                ""
            )
        )

        # Response
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

        error(
            handler,
            str(e)
        )


# =========================
# GET SINGLE ITEM
# GET /items/1
# =========================

def get_item(

    handler,
    item_id
):

    try:

        token = extract_token(
            handler
        )

        auth.authenticate_token(
            token
        )

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

        error(
            handler,
            str(e),
            404
        )


# =========================
# GET ALL ITEMS
# GET /items
# GET /items?page=1&limit=6
# GET /items?state=active
# =========================

def get_all_items(handler):

    try:

        token = extract_token(
            handler
        )

        auth.authenticate_token(
            token
        )

        # Query params
        parsed = urlparse(
            handler.path
        )

        query = parse_qs(
            parsed.query
        )

        # Pagination
        page = int(

            query.get(
                "page",
                [1]
            )[0]
        )

        limit = int(

            query.get(
                "limit",
                [6]
            )[0]
        )

        # State filter
        state = query.get(

            "state",

            [None]

        )[0]

        # Fetch items
        items = service.get_items_paginated(

            page,

            limit,

            state
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

            {

                "page": page,

                "limit": limit,

                "items": result
            }
        )

    except Exception as e:

        error(
            handler,
            str(e)
        )


# =========================
# UPDATE ITEM
# PUT /items/1
# =========================

def update_item(

    handler,
    item_id
):

    try:

        token = extract_token(
            handler
        )

        auth.authenticate_token(
            token
        )

        data = parse_json(
            handler
        )

        validate_item_payload(
            data
        )

        item = service.update_item(

            item_id,

            data["title"],

            data["details"]
        )

        success(

            handler,

            {

                "message":
                    "updated",

                "id":
                    item.id
            }
        )

    except Exception as e:

        error(
            handler,
            str(e)
        )


# =========================
# DELETE ITEM
# DELETE /items/1
# =========================

def delete_item(

    handler,
    item_id
):

    try:

        token = extract_token(
            handler
        )

        auth.authenticate_token(
            token
        )

        service.delete_item(
            item_id
        )

        success(

            handler,

            {

                "message":
                    "deleted"
            }
        )

    except Exception as e:

        error(
            handler,
            str(e)
        )