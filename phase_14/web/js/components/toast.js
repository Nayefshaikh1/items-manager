// web/js/components/toast.js

/* ========================= */
/* SHOW TOAST */
/* ========================= */

function showToast(

    message,

    isError = false
) {

    // Remove old toast
    const existingToast =

        document.querySelector(
            ".toast"
        );

    if (existingToast) {

        existingToast.remove();
    }

    // Create toast
    const toast =

        document.createElement(
            "div"
        );

    toast.className =

        isError
        ?
        "toast error-toast"
        :
        "toast success-toast";

    // Toast content
    toast.innerHTML = `

        <div class="
            toast-content
        ">

            <span class="
                toast-message
            ">

                ${message}

            </span>

            <button
                class="
                    toast-close
                "
            >

                ×

            </button>

        </div>
    `;

    // Add to body
    document.body.appendChild(
        toast
    );

    // Animate
    setTimeout(() => {

        toast.classList.add(
            "show-toast"
        );

    }, 10);

    // Close button
    toast
        .querySelector(
            ".toast-close"
        )
        .addEventListener(

            "click",

            () => {

                removeToast(
                    toast
                );
            }
        );

    // Auto remove
    setTimeout(() => {

        removeToast(
            toast
        );

    }, 3000);
}


/* ========================= */
/* REMOVE TOAST */
/* ========================= */

function removeToast(
    toast
) {

    if (!toast) {

        return;
    }

    toast.classList.remove(
        "show-toast"
    );

    setTimeout(() => {

        if (
            toast.parentNode
        ) {

            toast.remove();
        }

    }, 300);
}


/* ========================= */
/* SUCCESS SHORTCUT */
/* ========================= */

function showSuccess(
    message
) {

    showToast(
        message,
        false
    );
}


/* ========================= */
/* ERROR SHORTCUT */
/* ========================= */

function showError(
    message
) {

    showToast(
        message,
        true
    );
}