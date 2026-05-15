// web/js/pages/dashboard.js

requireAuth();

let currentPage = 1;
const LIMIT = 6;
let allItemsCache = [];

async function loadItems(forceRefresh = false) {
    const loadingBox = document.getElementById("loadingBox");
    const itemsGrid = document.getElementById("itemsGrid");
    const emptyState = document.getElementById("emptyState");
    const stateFilter = document.getElementById("stateFilter").value;

    loadingBox.classList.remove("hidden");
    itemsGrid.innerHTML = "";
    emptyState.classList.add("hidden");

    let url = `/items?page=${currentPage}&limit=${LIMIT}`;
    if (stateFilter) {
        url += `&state=${stateFilter}`;
    }

    const res = await api(url, "GET");

    loadingBox.classList.add("hidden");

    if (!res || !res.success) {
        showError(res ? res.error.message : "Failed to load items");
        return;
    }

    allItemsCache = res.data.items || [];
    applySearchFilter();
    
    // We only update summary when hitting the real API or if needed
    updateSummary();
}

function applySearchFilter() {
    const search = document.getElementById("searchInput").value.toLowerCase();
    
    let filtered = allItemsCache;
    if (search) {
        filtered = allItemsCache.filter(item => 
            (item.title && item.title.toLowerCase().includes(search)) ||
            (item.details && item.details.toLowerCase().includes(search))
        );
    }

    renderItems(filtered);
    renderPagination(filtered.length);
}

function renderItems(items) {
    const itemsGrid = document.getElementById("itemsGrid");
    const emptyState = document.getElementById("emptyState");

    itemsGrid.innerHTML = "";

    if (items.length === 0) {
        emptyState.classList.remove("hidden");
        return;
    }

    emptyState.classList.add("hidden");

    items.forEach(item => {
        const card = document.createElement("div");
        card.className = "card";
        
        let safeTitle = escapeHTML(item.title);
        let safeDetails = escapeHTML(item.details);
        if (safeDetails.length > 80) {
            safeDetails = safeDetails.substring(0, 80) + "...";
        }

        card.innerHTML = `
            <h3>${safeTitle}</h3>
            <span class="badge badge-${item.state}">${item.state}</span>
            <p style="margin-top: 10px;">${safeDetails}</p>
            <a href="/views/item.html?id=${item.id}" class="btn btn-primary btn-sm" style="display:inline-block; margin-top:10px;">View Details</a>
        `;
        itemsGrid.appendChild(card);
    });
}

function renderPagination(currentCount) {
    document.getElementById("pageInfo").innerText = `Page ${currentPage}`;
    
    document.getElementById("btnPrev").disabled = (currentPage === 1);
    
    // If we got fewer items than limit, we are on the last page
    document.getElementById("btnNext").disabled = (currentCount < LIMIT);
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        loadItems();
    }
}

function nextPage() {
    currentPage++;
    loadItems();
}

async function updateSummary() {
    const res = await api("/workflow/summary", "GET");
    if (res && res.success) {
        const summary = res.data;
        let total = 0;
        let draft = 0;
        let active = 0;
        let blocked = 0;
        let completed = 0;

        for (const [state, count] of Object.entries(summary)) {
            total += count;
            if (state === 'draft') draft = count;
            if (state === 'active') active = count;
            if (state === 'blocked') blocked = count;
            if (state === 'completed') completed = count;
        }

        document.getElementById("countTotal").innerText = total;
        document.getElementById("countDraft").innerText = draft;
        document.getElementById("countActive").innerText = active;
        document.getElementById("countBlocked").innerText = blocked;
        document.getElementById("countCompleted").innerText = completed;
    }
}

// Event Listeners
document.getElementById("searchInput").addEventListener("input", applySearchFilter);
document.getElementById("stateFilter").addEventListener("change", () => {
    currentPage = 1;
    loadItems();
});

// Init
loadItems();