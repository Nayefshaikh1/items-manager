// web/js/pages/edit_item.js

requireAuth();

const params = new URLSearchParams(window.location.search);
const itemId = params.get("id");

if (!itemId) {
    showErrorState("Invalid ID", "No item ID provided in URL.");
} else {
    loadItem();
}

async function loadItem() {
    const res = await api(`/items/${itemId}`, "GET");

    document.getElementById("loadingBox").classList.add("hidden");

    if (!res || !res.success) {
        showErrorState("Item Not Found", res ? res.error.message : "Failed to load item.");
        return;
    }

    document.getElementById("itemTitle").value = res.data.title;
    document.getElementById("itemDetails").value = res.data.details || "";
    document.getElementById("contentBox").classList.remove("hidden");
}

async function doSave() {
    const title = document.getElementById("itemTitle").value.trim();
    const details = document.getElementById("itemDetails").value.trim();
    const msg = document.getElementById("editMsg");

    msg.innerHTML = "";

    if (!title) {
        msg.innerHTML = `<div class="msg-error">Title is required</div>`;
        return;
    }

    const btn = document.getElementById("btnSave");
    btn.disabled = true;
    btn.innerText = "Saving...";

    const res = await api(`/items/${itemId}`, "PUT", { title, details });

    btn.disabled = false;
    btn.innerText = "Save Changes";

    if (res && res.success) {
        showSuccess("Item updated successfully!");
        setTimeout(() => goBack(), 1000);
    } else if (res) {
        msg.innerHTML = `<div class="msg-error">${escapeHTML(res.error.message)}</div>`;
    }
}

function goBack() {
    window.location.href = `/views/item.html?id=${itemId}`;
}

function showErrorState(title, msg) {
    document.getElementById("loadingBox").classList.add("hidden");
    document.getElementById("contentBox").classList.add("hidden");
    
    const errBox = document.getElementById("errorBox");
    errBox.classList.remove("hidden");
    
    document.getElementById("errorTitle").innerText = title;
    document.getElementById("errorMsg").innerText = msg;
}