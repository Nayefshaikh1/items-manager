function renderSummaryPanel(
    items
) {

    let draft = 0;

    let active = 0;

    let blocked = 0;

    let completed = 0;

    items.forEach(item => {

        if (
            item.state === "draft"
        ) {
            draft++;
        }

        if (
            item.state === "active"
        ) {
            active++;
        }

        if (
            item.state === "blocked"
        ) {
            blocked++;
        }

        if (
            item.state === "completed"
        ) {
            completed++;
        }
    });

    return `

        <div class="summary-grid">

            <div class="
                summary-card
            ">

                <h3>Total</h3>

                <p>
                    ${items.length}
                </p>

            </div>

            <div class="
                summary-card draft
            ">

                <h3>Draft</h3>

                <p>
                    ${draft}
                </p>

            </div>

            <div class="
                summary-card active
            ">

                <h3>Active</h3>

                <p>
                    ${active}
                </p>

            </div>

            <div class="
                summary-card blocked
            ">

                <h3>Blocked</h3>

                <p>
                    ${blocked}
                </p>

            </div>

            <div class="
                summary-card completed
            ">

                <h3>Completed</h3>

                <p>
                    ${completed}
                </p>

            </div>

        </div>
    `;
}