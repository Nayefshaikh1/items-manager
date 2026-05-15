// web/js/services/api.js

const API_BASE =
    "http://127.0.0.1:8000";


/* ========================= */
/* API REQUEST */
/* ========================= */

async function apiRequest(

    endpoint,

    method = "GET",

    body = null
) {

    const token =

        localStorage.getItem(
            "token"
        );

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

    const options = {

        method,
        headers
    };

    // Add body
    if (body) {

        options.body =
            JSON.stringify(body);
    }

    try {

        const response =

            await fetch(

                API_BASE + endpoint,

                options
            );

        // Parse JSON safely
        let data;

        try {

            data =
                await response.json();

        } catch {

            data = {

                success: false,

                error: {
                    message:
                        "Invalid server response"
                }
            };
        }

        // Unauthorized
        if (
            response.status === 401
        ) {

            localStorage.removeItem(
                "token"
            );

            window.location =
                "login.html";

            return;
        }

        // Not found
        if (
            response.status === 404
        ) {

            return {

                success: false,

                error: {
                    message:
                        "Resource not found"
                }
            };
        }

        // Server error
        if (
            response.status >= 500
        ) {

            return {

                success: false,

                error: {
                    message:
                        "Internal server error"
                }
            };
        }

        return data;

    } catch (error) {

        console.error(
            "API ERROR:",
            error
        );

        return {

            success: false,

            error: {
                message:
                    "Cannot connect to backend"
            }
        };
    }
}


/* ========================= */
/* GET REQUEST */
/* ========================= */

async function apiGet(
    endpoint
) {

    return await apiRequest(
        endpoint,
        "GET"
    );
}


/* ========================= */
/* POST REQUEST */
/* ========================= */

async function apiPost(
    endpoint,
    body
) {

    return await apiRequest(

        endpoint,

        "POST",

        body
    );
}


/* ========================= */
/* PUT REQUEST */
/* ========================= */

async function apiPut(
    endpoint,
    body
) {

    return await apiRequest(

        endpoint,

        "PUT",

        body
    );
}


/* ========================= */
/* DELETE REQUEST */
/* ========================= */

async function apiDelete(
    endpoint
) {

    return await apiRequest(

        endpoint,

        "DELETE"
    );
}