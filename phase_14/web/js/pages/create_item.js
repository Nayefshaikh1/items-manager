// web/js/pages/create_item.js

requireAuth();

async function doCreate() {
    const title = document.getElementById("itemTitle").value.trim();
    const details = document.getElementById("itemDetails").value.trim();
    const msg = document.getElementById("createMsg");

    msg.innerHTML = "";

    if (!title) {
        msg.innerHTML = `<div class="msg-error">Title is required</div>`;
        return;
    }

    const btn = document.getElementById("btnCreate");
    btn.disabled = true;
    btn.innerText = "Creating...";

    const res = await api("/items", "POST", { title, details });

    btn.disabled = false;
    btn.innerText = "Create Item";

    if (res && res.success) {
        showSuccess("Item created successfully!");
        setTimeout(() => {
            window.location.href = "/views/dashboard.html";
        }, 1000);
    } else if (res) {
        msg.innerHTML = `<div class="msg-error">${escapeHTML(res.error.message)}</div>`;
    }
}