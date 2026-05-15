DEFAULT_STATE = "draft"


ALLOWED_TRANSITIONS = {

    "draft": {"active"},

    "active": {
        "blocked",
        "completed"
    },

    "blocked": {"active"},

    # reopen support
    "completed": {"active"}
}