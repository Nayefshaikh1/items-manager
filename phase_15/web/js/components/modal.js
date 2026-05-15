function renderModal(
    title,
    content
) {

    return `

        <div class="
            modal-overlay
        ">

            <div class="
                modal
            ">

                <h2>
                    ${title}
                </h2>

                <div>

                    ${content}

                </div>

                <button
                    onclick="
                        closeModal()
                    "
                >
                    Close
                </button>

            </div>

        </div>
    `;
}


function openModal(
    title,
    content
) {

    const modalContainer =
        document.getElementById(
            "modalContainer"
        );

    modalContainer.innerHTML =
        renderModal(
            title,
            content
        );
}


function closeModal() {

    document.getElementById(
        "modalContainer"
    ).innerHTML = "";
}