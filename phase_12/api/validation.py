# api/validation.py


# ---------- CREATE ITEM VALIDATION ----------

def validate_item_payload(data):

    # Request must be dictionary
    if not isinstance(data, dict):

        raise ValueError(
            "Invalid JSON body"
        )

    # ---------- TITLE ----------

    # title required
    if "title" not in data:

        raise ValueError(
            "title is required"
        )

    # title must be string
    if not isinstance(
        data["title"],
        str
    ):

        raise ValueError(
            "title must be string"
        )

    # title cannot be empty
    if not data["title"].strip():

        raise ValueError(
            "title cannot be empty"
        )

    # ---------- DETAILS ----------

    # Optional details validation
    if (
        "details" in data
        and not isinstance(
            data["details"],
            str
        )
    ):

        raise ValueError(
            "details must be string"
        )


# ---------- UPDATE ITEM VALIDATION ----------

def validate_update_payload(data):

    if not isinstance(data, dict):

        raise ValueError(
            "Invalid JSON body"
        )

    # title required
    if "title" not in data:

        raise ValueError(
            "title is required"
        )

    # details required
    if "details" not in data:

        raise ValueError(
            "details is required"
        )

    # title type
    if not isinstance(
        data["title"],
        str
    ):

        raise ValueError(
            "title must be string"
        )

    # details type
    if not isinstance(
        data["details"],
        str
    ):

        raise ValueError(
            "details must be string"
        )

    # title empty
    if not data["title"].strip():

        raise ValueError(
            "title cannot be empty"
        )