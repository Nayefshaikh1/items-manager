function renderError(
    message
) {

    return `

        <div class="
            error-box
        ">

            ${message}

        </div>
    `;
}


function showError(
    containerId,
    message
) {

    document.getElementById(
        containerId
    ).innerHTML = renderError(
        message
    );
}