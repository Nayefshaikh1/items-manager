# UI Test — Login Page

## File Under Test
`web/views/login.html` + `web/js/pages/login.js`

---

## Test 1 — Page Load

**Steps:**
1. Open `login.html` in the browser

**Expected:**
- The page displays a centered auth card
- Title "Phase 13" is visible
- Subtitle "Workflow Management System" is visible
- Login tab is active (highlighted blue)
- Register tab is inactive (gray)
- Username and Password input fields are visible
- Login button is visible
- No error messages are shown

---

## Test 2 — Tab Switching

**Steps:**
1. Open `login.html`
2. Click the "Register" tab
3. Click the "Login" tab

**Expected:**
- Step 2: Register form appears (username, password, role dropdown), login form hides
- Step 2: Register tab turns blue, Login tab turns gray
- Step 3: Login form reappears, register form hides
- Step 3: Login tab turns blue, Register tab turns gray

---

## Test 3 — Login With Empty Fields

**Steps:**
1. Leave both username and password fields empty
2. Click the Login button

**Expected:**
- Message "All login fields required" appears
- No API request is sent
- User stays on the login page

---

## Test 4 — Login With Wrong Credentials

**Steps:**
1. Type "wronguser" in the username field
2. Type "wrongpass" in the password field
3. Click the Login button

**Expected:**
- Loading spinner appears briefly
- Error message "Invalid username" appears in the message area
- User stays on the login page

---

## Test 5 — Login With Correct Credentials

**Steps:**
1. Type a valid registered username
2. Type the correct password
3. Click the Login button

**Expected:**
- Loading spinner appears
- Message "Login successful" appears (green success box)
- After ~1 second, user is redirected to `dashboard.html`
- Token is saved in localStorage

---

## Test 6 — Register With Empty Fields

**Steps:**
1. Click the "Register" tab
2. Leave username and password empty
3. Click the Register button

**Expected:**
- Message "All register fields required" appears
- No API request is sent

---

## Test 7 — Register Successfully

**Steps:**
1. Click the "Register" tab
2. Enter a new unique username
3. Enter a password
4. Select a role (User or Admin)
5. Click the Register button

**Expected:**
- Loading spinner appears
- Message "Registration successful" appears (green)
- Form automatically switches to the Login tab
- The user can now log in with the new credentials

---

## Test 8 — Register Duplicate User

**Steps:**
1. Click the "Register" tab
2. Enter a username that already exists
3. Enter any password
4. Click the Register button

**Expected:**
- Error message "User already exists" appears (red)
- User stays on the register form

---

## Test 9 — Redirect When Already Logged In

**Steps:**
1. Login successfully (token is saved)
2. Navigate back to `login.html` manually

**Expected:**
- User is automatically redirected to `dashboard.html`
- Login page does not show

---

## Test 10 — Server Down

**Steps:**
1. Stop the backend server
2. Try to login with any credentials

**Expected:**
- Loading spinner appears then disappears
- Message "Server connection failed" appears
- App does not crash
