function showLoading() {

    document
        .getElementById(
            "loading"
        )
        .classList.remove(
            "hidden"
        );
}

function hideLoading() {

    document
        .getElementById(
            "loading"
        )
        .classList.add(
            "hidden"
        );
}