// web/js/api.js

const API = "http://127.0.0.1:8000";

function getToken() {
    return localStorage.getItem("token");
}

function setToken(token) {
    localStorage.setItem("token", token);
}

function clearToken() {
    localStorage.removeItem("token");
}

async function api(endpoint, method, body) {

    const headers = {
        "Content-Type": "application/json"
    };

    const token = getToken();

    if (token) {
        headers["Authorization"] = "Bearer " + token;
    }

    const options = { method, headers };

    if (body) {
        options.body = JSON.stringify(body);
    }

    try {

        const res = await fetch(
            API + endpoint,
            options
        );

        const data = await res.json().catch(
            () => ({
                success: false,
                error: { message: "Bad response" }
            })
        );

        if (res.status === 401) {
            clearToken();
            window.location.href = "/views/login.html";
            return null;
        }

        return data;

    } catch (err) {

        return {
            success: false,
            error: {
                message: "Cannot connect to server"
            }
        };
    }
}
