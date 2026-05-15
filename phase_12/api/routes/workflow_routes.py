# api/routes/workflow_routes.py

from app_context import (
    service,
    auth
)

from api.response import (
    success,
    error
)

from api.auth_middleware import (
    extract_token
)


# ---------- CHANGE STATE ----------

# POST /items/1/active
# POST /items/1/completed
def change_state(
    handler,
    item_id,
    new_state
):

    try:

        # Extract token
        token = extract_token(handler)

        # Authenticate user
        auth.authenticate_token(token)

        # Transition item
        item = service.transition_item(
            item_id,
            new_state
        )

        success(
            handler,
            {
                "id": item.id,
                "new_state": item.state
            }
        )

    except Exception as e:

        error(handler, str(e))


# ---------- GET WORKFLOW HISTORY ----------

# GET /items/1/history
def get_history(
    handler,
    item_id
):

    try:

        token = extract_token(handler)

        auth.authenticate_token(token)

        history = service.get_history(
            item_id
        )

        result = []

        for row in history:

            result.append({

                "old_state":
                row["old_state"],

                "new_state":
                row["new_state"],

                "changed_at":
                row["changed_at"]
            })

        success(
            handler,
            result
        )

    except Exception as e:

        error(handler, str(e))


# ---------- WORKFLOW SUMMARY ----------

# GET /workflow/summary
def workflow_summary(handler):

    try:

        token = extract_token(handler)

        auth.authenticate_token(token)

        summary = (
            service.workflow_summary()
        )

        success(
            handler,
            summary
        )

    except Exception as e:

        error(handler, str(e))