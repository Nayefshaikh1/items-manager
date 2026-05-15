async function changeState(
    state
) {

    const result =
        await apiRequest(
            `/items/${itemId}/${state}`,
            "POST"
        );

    if (result.success) {

        alert(
            "Workflow updated"
        );

        location.reload();

    } else {

        alert(
            result.error.message
        );
    }
}


async function loadHistory() {

    const result =
        await apiRequest(
            `/items/${itemId}/history`
        );

    const container =
        document.getElementById(
            "historyContainer"
        );

    container.innerHTML = "";

    result.data.forEach(row => {

        container.innerHTML += `

            <div class="
                history-item
            ">

                <strong>
                    ${row.old_state}
                </strong>

                →

                <strong>
                    ${row.new_state}
                </strong>

                <br>

                <small>
                    ${row.changed_at}
                </small>

            </div>
        `;
    });
}