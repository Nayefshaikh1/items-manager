# UI Test — Item Details Page

## File Under Test
`web/views/item.html` + `web/js/pages/item_details.js`

---

## Test 1 — Page Load With Valid Item

**Steps:**
1. Login successfully
2. Navigate to `item.html?id=1` (use a valid item ID)

**Expected:**
- Loading spinner appears briefly
- Item title is displayed as a heading
- Workflow state badge is visible with correct color
- Item details text is shown
- "Edit" button is visible, linking to `edit.html?id=1`
- "Delete" button (red) is visible
- Workflow action buttons are shown below the item card
- Workflow History section is visible at the bottom

---

## Test 2 — Page Load With Invalid Item ID

**Steps:**
1. Navigate to `item.html?id=99999`

**Expected:**
- Error message "Item not found" or "Resource not found" is displayed
- "Back to Dashboard" button is visible
- No item card is rendered

---

## Test 3 — Page Load With No ID

**Steps:**
1. Navigate to `item.html` (no ?id= parameter)

**Expected:**
- Error message "Invalid item ID" is displayed
- "Back to Dashboard" button is visible

---

## Test 4 — Edit Button Navigation

**Steps:**
1. Open a valid item detail page
2. Click the "Edit" button

**Expected:**
- Browser navigates to `edit.html?id=<item_id>`
- The edit form loads with pre-filled data

---

## Test 5 — Delete Item

**Steps:**
1. Open a valid item detail page
2. Click the "Delete" button

**Expected:**
- A browser confirm dialog appears: "Delete this item?"
- Click "OK": loading spinner appears
- Success toast "Item deleted" appears
- After ~800ms, user is redirected to `dashboard.html`
- The item is no longer in the dashboard list

---

## Test 6 — Delete Item Cancelled

**Steps:**
1. Open a valid item detail page
2. Click the "Delete" button
3. Click "Cancel" on the confirm dialog

**Expected:**
- No API request is sent
- Item remains on the page
- No changes occur

---

## Test 7 — Workflow History Empty

**Steps:**
1. Create a new item (state = draft)
2. Open its detail page

**Expected:**
- Workflow History section shows "No workflow history"
- No history cards are displayed

---

## Test 8 — Workflow History With Entries

**Steps:**
1. Create an item and perform state changes (e.g., draft → active → blocked)
2. Open the item's detail page

**Expected:**
- Workflow History section shows history cards
- Each card shows: old_state → new_state with timestamp
- Most recent transition appears first
- Arrow (→) separates old and new states

---

## Test 9 — Edit Form Pre-Fill

**Steps:**
1. Open `item.html?id=1`
2. Click "Edit"

**Expected:**
- Edit page loads at `edit.html?id=1`
- Title input is pre-filled with the current title
- Details textarea is pre-filled with the current details

---

## Test 10 — Save Edited Item

**Steps:**
1. Open `edit.html?id=1`
2. Change the title to "Updated Title"
3. Change the details to "Updated Details"
4. Click "Save Changes"

**Expected:**
- API receives PUT /items/1 with updated data
- User is redirected to `item.html?id=1`
- The item detail page shows the new title and details

---

## Test 11 — Save Edit With Empty Title

**Steps:**
1. Open `edit.html?id=1`
2. Clear the title field
3. Click "Save Changes"

**Expected:**
- Error message appears: "title cannot be empty"
- User stays on the edit page
- Item is not updated

---

## Test 12 — Unauthenticated Access

**Steps:**
1. Clear localStorage (remove token)
2. Navigate to `item.html?id=1`

**Expected:**
- API returns 401
- User is redirected to `login.html`
