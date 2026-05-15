/* ========================= */
/* REQUIRED */
/* ========================= */

function isRequired(value) {

    return (
        value !== null
        &&
        value !== undefined
        &&
        value.trim() !== ""
    );
}


/* ========================= */
/* MIN LENGTH */
/* ========================= */

function minLength(
    value,
    min
) {

    return (
        value.trim().length >= min
    );
}


/* ========================= */
/* VALID EMAIL */
/* ========================= */

function isValidEmail(
    email
) {

    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        .test(email);
}


/* ========================= */
/* VALIDATE LOGIN */
/* ========================= */

function validateLogin(
    username,
    password
) {

    const errors = [];

    if (
        !isRequired(username)
    ) {

        errors.push(
            "Username required"
        );
    }

    if (
        !isRequired(password)
    ) {

        errors.push(
            "Password required"
        );
    }

    return errors;
}


/* ========================= */
/* VALIDATE REGISTER */
/* ========================= */

function validateRegister(
    username,
    password
) {

    const errors = [];

    if (
        !isRequired(username)
    ) {

        errors.push(
            "Username required"
        );
    }

    if (
        !minLength(username, 3)
    ) {

        errors.push(
            "Username too short"
        );
    }

    if (
        !isRequired(password)
    ) {

        errors.push(
            "Password required"
        );
    }

    if (
        !minLength(password, 6)
    ) {

        errors.push(
            "Password must be at least 6 characters"
        );
    }

    return errors;
}


/* ========================= */
/* VALIDATE ITEM */
/* ========================= */

function validateItem(
    title,
    details
) {

    const errors = [];

    if (
        !isRequired(title)
    ) {

        errors.push(
            "Title required"
        );
    }

    if (
        !minLength(title, 3)
    ) {

        errors.push(
            "Title too short"
        );
    }

    if (
        !isRequired(details)
    ) {

        errors.push(
            "Details required"
        );
    }

    return errors;
}