WORKFLOW_STATES = {
    "draft",
    "active",
    "blocked",
    "completed",
    "archived"
}


DEFAULT_STATE = "draft"


ALLOWED_TRANSITIONS = {

    "draft": {
        "active",
        "archived"
    },

    "active": {
        "blocked",
        "completed"
    },

    "blocked": {
        "active",
        "archived"
    },

    "completed": {
        "active",
        "archived"
    },

    "archived": set()
}