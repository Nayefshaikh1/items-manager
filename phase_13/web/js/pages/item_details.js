// web/js/pages/item_details.js

requireAuth();

const params = new URLSearchParams(window.location.search);
const itemId = params.get("id");

if (!itemId) {
    showErrorState("Invalid ID", "No item ID provided in URL.");
} else {
    loadItem();
}

async function loadItem() {
    document.getElementById("loadingBox").classList.remove("hidden");
    document.getElementById("contentBox").classList.add("hidden");
    document.getElementById("errorBox").classList.add("hidden");

    const res = await api(`/items/${itemId}`, "GET");

    document.getElementById("loadingBox").classList.add("hidden");

    if (!res || !res.success) {
        showErrorState("Item Not Found", res ? res.error.message : "Failed to load item.");
        return;
    }

    const item = res.data;
    
    document.getElementById("itemTitle").innerText = item.title;
    document.getElementById("itemDetails").innerText = item.details || "No details provided.";
    
    const badge = document.getElementById("itemBadge");
    badge.innerText = item.state;
    badge.className = `badge badge-${item.state}`;

    document.getElementById("contentBox").classList.remove("hidden");

    renderWorkflowActions(item.state);
    loadHistory();
}

function renderWorkflowActions(state) {
    const container = document.getElementById("workflowActions");
    container.innerHTML = "";

    if (state === "draft") {
        container.innerHTML += `<button class="btn btn-primary" onclick="changeState('active')">Activate</button>`;
    } else if (state === "active") {
        container.innerHTML += `<button class="btn btn-danger" onclick="changeState('blocked')">Block</button>`;
        container.innerHTML += `<button class="btn btn-success" onclick="changeState('completed')">Complete</button>`;
    } else if (state === "blocked") {
        container.innerHTML += `<button class="btn btn-primary" onclick="changeState('active')">Reactivate</button>`;
    } else if (state === "completed") {
        container.innerHTML += `<button class="btn btn-primary" onclick="changeState('active')">Reopen</button>`;
    }
}

async function changeState(newState) {
    showToast("Updating state...");
    const res = await api(`/items/${itemId}/${newState}`, "POST");
    
    if (res && res.success) {
        showSuccess(`Item changed to ${newState}`);
        loadItem();
    } else if (res) {
        showError(res.error.message);
    }
}

async function loadHistory() {
    const container = document.getElementById("historyList");
    container.innerHTML = `<div style="color:#666">Loading history...</div>`;

    const res = await api(`/items/${itemId}/history`, "GET");

    if (!res || !res.success) {
        container.innerHTML = `<div style="color:red">Failed to load history</div>`;
        return;
    }

    const history = res.data;
    if (history.length === 0) {
        container.innerHTML = `<div style="color:#666">No workflow history available.</div>`;
        return;
    }

    container.innerHTML = "";
    history.forEach(h => {
        const d = new Date(h.changed_at).toLocaleString();
        container.innerHTML += `
            <div class="history-entry">
                <div>
                    <span class="badge badge-${h.old_state}">${h.old_state}</span>
                    <span style="margin: 0 10px;">&rarr;</span>
                    <span class="badge badge-${h.new_state}">${h.new_state}</span>
                </div>
                <div style="color:#888; font-size:12px;">${d}</div>
            </div>
        `;
    });
}

function goEdit() {
    window.location.href = `/views/edit.html?id=${itemId}`;
}

async function doDelete() {
    if (!confirm("Are you sure you want to delete this item?")) return;

    document.getElementById("btnDelete").disabled = true;
    const res = await api(`/items/${itemId}`, "DELETE");

    if (res && res.success) {
        showSuccess("Item deleted");
        setTimeout(() => {
            window.location.href = "/views/dashboard.html";
        }, 1000);
    } else {
        document.getElementById("btnDelete").disabled = false;
        showError(res ? res.error.message : "Failed to delete");
    }
}

function showErrorState(title, msg) {
    document.getElementById("loadingBox").classList.add("hidden");
    document.getElementById("contentBox").classList.add("hidden");
    
    const errBox = document.getElementById("errorBox");
    errBox.classList.remove("hidden");
    
    document.getElementById("errorTitle").innerText = title;
    document.getElementById("errorMsg").innerText = msg;
}