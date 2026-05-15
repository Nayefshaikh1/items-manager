function renderNavbar() {

    return `

        <header class="topbar">

            <div>

                <h1>
                    Phase 13 Dashboard
                </h1>

                <p>
                    Workflow Management System
                </p>

            </div>

            <div>

                <button
                    onclick="goDashboard()"
                >
                    Dashboard
                </button>

                <button
                    onclick="goCreate()"
                >
                    Create
                </button>

                <button
                    onclick="logout()"
                >
                    Logout
                </button>

            </div>

        </header>
    `;
}


function goDashboard() {

    window.location =
        "dashboard.html";
}


function goCreate() {

    window.location =
        "create.html";
}