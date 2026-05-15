# api/router.py

from api.response import success

from api.routes.auth_routes import (
    register,
    login
)

from api.routes.item_routes import (
    create_item,
    get_item,
    get_all_items,
    update_item,
    delete_item
)

from api.routes.workflow_routes import (
    change_state,
    get_history,
    workflow_summary
)


class Router:

    def handle(
        self,
        handler,
        method
    ):

        # Remove query parameters
        path = handler.path.split("?")[0]

        # Split route safely
        parts = path.strip("/").split("/")

        # ---------- AUTH ----------

        # POST /register
        if (
            path == "/register"
            and method == "POST"
        ):

            return register(handler)

        # POST /login
        if (
            path == "/login"
            and method == "POST"
        ):

            return login(handler)

        # ---------- ITEMS ----------

        # GET /items
        if (
            path.startswith("/items")
            and method == "GET"
        ):

            # GET /items
            if len(parts) == 1:

                return get_all_items(
                    handler
                )

            # GET /items/1
            if (
                len(parts) == 2
                and parts[1].isdigit()
            ):

                return get_item(
                    handler,
                    int(parts[1])
                )

            # GET /items/1/history
            if (
                len(parts) == 3
                and parts[2] == "history"
            ):

                return get_history(
                    handler,
                    int(parts[1])
                )

        # POST /items
        if (
            path == "/items"
            and method == "POST"
        ):

            return create_item(
                handler
            )

        # POST /items/1/active
        if (
            len(parts) == 3
            and method == "POST"
            and parts[0] == "items"
            and parts[1].isdigit()
        ):

            return change_state(
                handler,
                int(parts[1]),
                parts[2]
            )

        # PUT /items/1
        if (
            len(parts) == 2
            and method == "PUT"
            and parts[0] == "items"
            and parts[1].isdigit()
        ):

            return update_item(
                handler,
                int(parts[1])
            )

        # DELETE /items/1
        if (
            len(parts) == 2
            and method == "DELETE"
            and parts[0] == "items"
            and parts[1].isdigit()
        ):

            return delete_item(
                handler,
                int(parts[1])
            )

        # ---------- WORKFLOW ----------

        # GET /workflow/summary
        if (
            path == "/workflow/summary"
            and method == "GET"
        ):

            return workflow_summary(
                handler
            )

        # ---------- 404 ----------

        handler.send_response(404)

        handler.end_headers()