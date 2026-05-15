function renderEmptyState() {

    return `

        <div class="
            empty-state
        ">

            <h2>
                No Items Found
            </h2>

            <p>
                Create your first item
                to get started.
            </p>

        </div>
    `;
}


function showEmpty(
    containerId
) {

    document.getElementById(
        containerId
    ).innerHTML =
        renderEmptyState();
}