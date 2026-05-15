# UI Test — Create Item Page

## File Under Test
`web/views/create.html` + `web/js/pages/create_item.js`

---

## Test 1 — Page Load

**Steps:**
1. Login successfully
2. Navigate to `create.html`

**Expected:**
- A centered form card is displayed
- Title "Create Item" is visible
- Title input field with placeholder "Title" is present
- Details textarea with placeholder "Details" is present
- "Create Item" button is visible
- No error messages are shown

---

## Test 2 — Create Item Successfully

**Steps:**
1. Type "My New Item" in the title field
2. Type "This is a test item" in the details field
3. Click the "Create Item" button

**Expected:**
- API receives POST /items with correct payload
- User is redirected to `dashboard.html`
- The new item appears in the dashboard list
- The new item has state "draft"

---

## Test 3 — Create Item With Empty Title

**Steps:**
1. Leave the title field empty
2. Type something in details
3. Click the "Create Item" button

**Expected:**
- Error message appears: "title cannot be empty" or "title is required"
- Error is shown in the message area (red error-box)
- User stays on the create page
- No item is created

---

## Test 4 — Create Item With Empty Details

**Steps:**
1. Type a title
2. Leave the details field empty
3. Click the "Create Item" button

**Expected:**
- Item is created successfully (details is optional)
- User is redirected to the dashboard
- The item appears with empty details

---

## Test 5 — Create Item Without Authentication

**Steps:**
1. Clear localStorage (remove token)
2. Navigate to `create.html`
3. Fill in fields and click "Create Item"

**Expected:**
- The API returns 401
- User is redirected to `login.html`

---

## Test 6 — Server Error During Creation

**Steps:**
1. Stop the backend server
2. Fill in the form and click "Create Item"

**Expected:**
- Error message appears: "Cannot connect to backend"
- User stays on the create page
- Form data is preserved

---

## Test 7 — Multiple Rapid Submissions

**Steps:**
1. Fill in valid data
2. Click "Create Item" multiple times quickly

**Expected:**
- Only one item is created
- User is redirected after the first successful creation
- No duplicate items appear in the dashboard
