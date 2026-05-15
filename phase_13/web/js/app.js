// web/js/app.js

/* ========================= */
/* APP START */
/* ========================= */

document.addEventListener(

    "DOMContentLoaded",

    () => {

        initializeApp();
    }
);


/* ========================= */
/* INITIALIZE */
/* ========================= */

function initializeApp() {

    console.log(
        "Phase 13 Started"
    );

    createGlobalLoader();

    checkAuthPage();
}


/* ========================= */
/* AUTH CHECK */
/* ========================= */

function checkAuthPage() {

    const token =

        localStorage.getItem(
            "token"
        );

    const path =
        window.location.pathname;

    const isLoginPage =

        path.includes(
            "login.html"
        );

    // Already logged in
    if (
        token &&
        isLoginPage
    ) {

        window.location =
            "/views/dashboard.html";

        return;
    }

    // Protected pages
    if (
        !token &&
        !isLoginPage
    ) {

        const publicPages = [

            "login.html"
        ];

        const allowed =
            publicPages.some(
                page =>
                    path.includes(page)
            );

        if (!allowed) {

            window.location =
                "/views/login.html";
        }
    }
}


/* ========================= */
/* DOM HELPERS */
/* ========================= */

function qs(id) {

    return document.getElementById(
        id
    );
}


function clearElement(id) {

    const el = qs(id);

    if (el) {

        el.innerHTML = "";
    }
}


/* ========================= */
/* TOKEN HELPERS */
/* ========================= */

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
/* LOGOUT */
/* ========================= */

function logout() {

    removeToken();

    showSuccess(
        "Logged out"
    );

    setTimeout(() => {

        window.location =
            "/views/login.html";

    }, 500);
}


/* ========================= */
/* CREATE GLOBAL LOADER */
/* ========================= */

function createGlobalLoader() {

    // Already exists
    if (
        document.getElementById(
            "globalLoader"
        )
    ) {

        return;
    }

    const loader =

        document.createElement(
            "div"
        );

    loader.id =
        "globalLoader";

    loader.className =
        "global-loader hidden";

    loader.innerHTML = `

        <div class="
            loading-overlay
        ">

            <div class="
               loader-content
            ">

                <div class="
                    spinner
                "></div>

                <p>
                    Loading...
                </p>

            </div>

        </div>
    `;

    document.body.appendChild(
        loader
    );
}


/* ========================= */
/* SHOW LOADER */
/* ========================= */

function showGlobalLoading() {

    const loader =

        document.getElementById(
            "globalLoader"
        );

    if (!loader) {

        return;
    }

    loader.classList.remove(
        "hidden"
    );
}


/* ========================= */
/* HIDE LOADER */
/* ========================= */

function hideGlobalLoading() {

    const loader =

        document.getElementById(
            "globalLoader"
        );

    if (!loader) {

        return;
    }

    loader.classList.add(
        "hidden"
    );
}


/* ========================= */
/* SUCCESS */
/* ========================= */

function showSuccess(
    message
) {

    if (
        typeof showToast ===
        "function"
    ) {

        showToast(
            message,
            false
        );

        return;
    }

    console.log(
        "SUCCESS:",
        message
    );
}


/* ========================= */
/* ERROR */
/* ========================= */

function showError(
    message
) {

    if (
        typeof showToast ===
        "function"
    ) {

        showToast(
            message,
            true
        );

        return;
    }

    console.error(
        "ERROR:",
        message
    );

    alert(message);
}