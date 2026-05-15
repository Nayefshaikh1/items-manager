/* ========================= */
/* DATE FORMAT */
/* ========================= */

function formatDate(date) {

    if (!date) {

        return "N/A";
    }

    return new Date(
        date
    ).toLocaleString();
}


/* ========================= */
/* CAPITALIZE */
/* ========================= */

function capitalize(text) {

    if (!text) {

        return "";
    }

    return (
        text.charAt(0)
        .toUpperCase()
        +
        text.slice(1)
    );
}


/* ========================= */
/* WORKFLOW LABEL */
/* ========================= */

function formatWorkflowState(
    state
) {

    switch (state) {

        case "draft":

            return "Draft";

        case "active":

            return "Active";

        case "blocked":

            return "Blocked";

        case "completed":

            return "Completed";

        default:

            return state;
    }
}


/* ========================= */
/* SHORT TEXT */
/* ========================= */

function truncateText(
    text,
    length = 120
) {

    if (!text) {

        return "";
    }

    if (
        text.length <= length
    ) {

        return text;
    }

    return (
        text.slice(0, length)
        + "..."
    );
}