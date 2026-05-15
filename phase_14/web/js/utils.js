// web/js/utils.js

function showToast(message, isError = false) {
    const existing = document.querySelector(".toast");
    if (existing) existing.remove();

    const toast = document.createElement("div");
    toast.className = "toast " + (isError ? "error" : "success");
    
    toast.innerHTML = `
        <span>${message}</span>
        <button class="close-toast">&times;</button>
    `;

    document.body.appendChild(toast);

    setTimeout(() => toast.classList.add("show"), 10);

    toast.querySelector(".close-toast").onclick = () => {
        toast.classList.remove("show");
        setTimeout(() => toast.remove(), 300);
    };

    setTimeout(() => {
        if (toast.parentNode) {
            toast.classList.remove("show");
            setTimeout(() => toast.remove(), 300);
        }
    }, 3000);
}

function showSuccess(msg) { showToast(msg, false); }
function showError(msg) { showToast(msg, true); }

function logout() {
    clearToken();
    window.location.href = "/views/login.html";
}

function requireAuth() {
    if (!getToken() && !window.location.pathname.includes("login.html")) {
        window.location.href = "/views/login.html";
    }
}

function escapeHTML(str) {
    if (!str) return "";
    return str.replace(/[&<>'"]/g, 
        tag => ({
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            "'": '&#39;',
            '"': '&quot;'
        }[tag] || tag)
    );
}
