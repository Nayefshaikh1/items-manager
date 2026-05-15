// web/js/services/auth.js

/* ========================= */
/* TOKEN STORAGE */
/* ========================= */

function saveToken(
    token
) {

    if (!token) {

        return;
    }

    localStorage.setItem(
        "token",
        token
    );
}


function getToken() {

    return localStorage.getItem(
        "token"
    );
}


function removeToken() {

    localStorage.removeItem(
        "token"
    );
}


/* ========================= */
/* AUTH STATUS */
/* ========================= */

function isLoggedIn() {

    return !!getToken();
}


/* ========================= */
/* LOGOUT */
/* ========================= */

function logout() {

    removeToken();

    showSuccess(
        "Logged out"
    );

    setTimeout(() => {

        window.location =
            "/views/login.html?logout=true";

    }, 500);
}


/* ========================= */
/* AUTH HEADER */
/* ========================= */

function getAuthHeaders() {

    const token =
        getToken();

    const headers = {

        "Content-Type":
            "application/json"
    };

    // Add token
    if (token) {

        headers[
            "Authorization"
        ] = `Bearer ${token}`;
    }

    return headers;
}


/* ========================= */
/* REQUIRE LOGIN */
/* ========================= */

function requireLogin() {

    const token =
        getToken();

    const currentPage =

        window.location.pathname;

    const isLoginPage =

        currentPage.includes(
            "login.html"
        );

    // Redirect if not logged in
    if (
        !token &&
        !isLoginPage
    ) {

        window.location =
    "/views/login.html";

        return;
    }

    // Redirect logged users
    if (
        token &&
        isLoginPage &&
        !window.location.search.includes(
            "logout"
        )
    ) {

        window.location =
    "/views/dashboard.html";
    }
}


/* ========================= */
/* SESSION CHECK */
/* ========================= */

function checkSession() {

    const token =
        getToken();

    // No token
    if (!token) {

        return false;
    }

    return true;
}


/* ========================= */
/* AUTO INIT */
/* ========================= */

document.addEventListener(

    "DOMContentLoaded",

    () => {

        requireLogin();
    }
);