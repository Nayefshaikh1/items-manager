// web/js/pages/login.js

// If already logged in, redirect
if (getToken()) {
    window.location.href = "/views/dashboard.html";
}

function switchTab(tab) {
    const loginForm = document.getElementById("loginForm");
    const regForm = document.getElementById("registerForm");
    const tabLogin = document.getElementById("tabLogin");
    const tabReg = document.getElementById("tabRegister");

    if (tab === 'login') {
        loginForm.classList.remove("hidden");
        regForm.classList.add("hidden");
        tabLogin.classList.add("active");
        tabReg.classList.remove("active");
        document.getElementById("loginMsg").innerHTML = "";
    } else {
        loginForm.classList.add("hidden");
        regForm.classList.remove("hidden");
        tabLogin.classList.remove("active");
        tabReg.classList.add("active");
        document.getElementById("regMsg").innerHTML = "";
    }
}

async function doLogin() {
    const user = document.getElementById("loginUser").value.trim();
    const pass = document.getElementById("loginPass").value.trim();
    const msg = document.getElementById("loginMsg");

    msg.innerHTML = "";

    if (!user || !pass) {
        msg.innerHTML = `<div class="msg-error">All login fields required</div>`;
        return;
    }

    const btn = document.getElementById("btnLogin");
    btn.disabled = true;
    btn.innerText = "Logging in...";

    const res = await api("/login", "POST", { username: user, password: pass });

    btn.disabled = false;
    btn.innerText = "Login";

    if (res && res.success) {
        setToken(res.data.token);
        msg.innerHTML = `<div class="msg-success">Login successful! Redirecting...</div>`;
        setTimeout(() => {
            window.location.href = "/views/dashboard.html";
        }, 1000);
    } else if (res) {
        msg.innerHTML = `<div class="msg-error">${escapeHTML(res.error.message)}</div>`;
    }
}

async function doRegister() {
    const user = document.getElementById("regUser").value.trim();
    const pass = document.getElementById("regPass").value.trim();
    const role = document.getElementById("regRole").value;
    const msg = document.getElementById("regMsg");

    msg.innerHTML = "";

    if (!user || !pass) {
        msg.innerHTML = `<div class="msg-error">All register fields required</div>`;
        return;
    }

    const btn = document.getElementById("btnRegister");
    btn.disabled = true;
    btn.innerText = "Registering...";

    const res = await api("/register", "POST", { username: user, password: pass, role: role });

    btn.disabled = false;
    btn.innerText = "Register";

    if (res && res.success) {
        msg.innerHTML = `<div class="msg-success">Registration successful!</div>`;
        setTimeout(() => {
            document.getElementById("loginUser").value = user;
            document.getElementById("loginPass").value = "";
            switchTab('login');
        }, 1500);
    } else if (res) {
        msg.innerHTML = `<div class="msg-error">${escapeHTML(res.error.message)}</div>`;
    }
}