function renderItemCard(item) {

    return `

        <div class="card">

            <h3>
                ${item.title}
            </h3>

            <p>
                ${item.details}
            </p>

            <span class="
                badge
                ${item.state}
            ">
                ${item.state}
            </span>

            <br><br>

            <a href="
                item.html?id=${item.id}
            ">
                View Details
            </a>

        </div>
    `;
}