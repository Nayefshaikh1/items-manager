/* ========================= */
/* DOM HELPERS */
/* ========================= */

function qs(id) {

    return document.getElementById(
        id
    );
}


function clearElement(id) {

    const element = qs(id);

    if (element) {

        element.innerHTML = "";
    }
}


/* ========================= */
/* URL HELPERS */
/* ========================= */

function getQueryParam(name) {

    const params =
        new URLSearchParams(
            window.location.search
        );

    return params.get(name);
}


/* ========================= */
/* NAVIGATION */
/* ========================= */

function redirect(url) {

    window.location = url;
}


/* ========================= */
/* TOKEN HELPERS */
/* ========================= */

function getToken() {

    return localStorage.getItem(
        "token"
    );
}


function saveToken(token) {

    localStorage.setItem(
        "token",
        token
    );
}


function removeToken() {

    localStorage.removeItem(
        "token"
    );
}


/* ========================= */
/* AUTH CHECK */
/* ========================= */

function requireAuth() {

    const token = getToken();

    if (!token) {

        redirect(
            "login.html"
        );
    }
}


/* ========================= */
/* LOGOUT */
/* ========================= */

function logout() {

    removeToken();

    redirect(
        "login.html"
    );
}


/* ========================= */
/* STRING HELPERS */
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
/* DATE FORMAT */
/* ========================= */

function formatDate(date) {

    return new Date(
        date
    ).toLocaleString();
}