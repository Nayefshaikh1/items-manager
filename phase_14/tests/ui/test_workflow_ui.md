# UI Test — Workflow Actions

## File Under Test
`web/views/item.html` + `web/js/pages/item_details.js`

---

## Test 1 — Draft Item Shows Only "Activate" Button

**Steps:**
1. Create a new item (default state = draft)
2. Open its detail page

**Expected:**
- Workflow buttons section shows: Activate, Block, Complete
- Only "Activate" is a valid transition from draft
- Clicking Block or Complete should result in an error from the API

---

## Test 2 — Activate a Draft Item

**Steps:**
1. Open a draft item's detail page
2. Click the "Activate" button

**Expected:**
- Loading spinner appears
- Success toast "Workflow updated" appears
- Page reloads automatically
- Badge changes from "draft" (gray) to "active" (blue)
- Workflow History shows a new entry: draft → active
- Available buttons update for the "active" state

---

## Test 3 — Block an Active Item

**Steps:**
1. Open an active item's detail page
2. Click the "Block" button

**Expected:**
- Loading spinner appears
- Success toast "Workflow updated" appears
- Page reloads automatically
- Badge changes from "active" (blue) to "blocked" (red)
- Workflow History shows: active → blocked
- Available buttons update for the "blocked" state

---

## Test 4 — Complete an Active Item

**Steps:**
1. Open an active item's detail page
2. Click the "Complete" button

**Expected:**
- Loading spinner appears
- Success toast "Workflow updated" appears
- Badge changes to "completed" (green)
- Workflow History shows: active → completed

---

## Test 5 — Reactivate a Blocked Item

**Steps:**
1. Open a blocked item's detail page
2. Click the "Activate" button

**Expected:**
- Badge changes from "blocked" (red) to "active" (blue)
- Workflow History shows: blocked → active
- Success toast appears

---

## Test 6 — Reopen a Completed Item

**Steps:**
1. Open a completed item's detail page
2. Click the "Activate" button (acts as Reopen)

**Expected:**
- Badge changes from "completed" (green) to "active" (blue)
- Workflow History shows: completed → active
- Success toast appears

---

## Test 7 — Invalid Transition (Draft → Blocked)

**Steps:**
1. Open a draft item's detail page
2. Click the "Block" button

**Expected:**
- Error toast appears with message: "Cannot move from draft to blocked"
- Badge stays as "draft" (gray)
- No history entry is added
- Page does not crash

---

## Test 8 — Invalid Transition (Draft → Completed)

**Steps:**
1. Open a draft item's detail page
2. Click the "Complete" button

**Expected:**
- Error toast appears: "Cannot move from draft to completed"
- Item state unchanged

---

## Test 9 — Workflow History Accumulates

**Steps:**
1. Create a new item (draft)
2. Activate it (draft → active)
3. Block it (active → blocked)
4. Reactivate it (blocked → active)
5. Complete it (active → completed)

**Expected:**
- Workflow History section shows 4 entries (most recent first):
  1. active → completed
  2. blocked → active
  3. active → blocked
  4. draft → active
- Each entry has a timestamp

---

## Test 10 — State Reflected on Dashboard

**Steps:**
1. Change an item's state via the detail page
2. Navigate back to the dashboard

**Expected:**
- The item's badge on the dashboard card shows the updated state
- Summary counts reflect the new state distribution
- Filter by the new state includes this item

---

## Test 11 — Workflow Action Without Authentication

**Steps:**
1. Clear localStorage (remove token)
2. Navigate to `item.html?id=1`
3. Click any workflow action button

**Expected:**
- API returns 401
- User is redirected to `login.html`

---

## Test 12 — Rapid Workflow Button Clicks

**Steps:**
1. Open an active item
2. Click "Complete" multiple times very quickly

**Expected:**
- Only one state change occurs
- No duplicate history entries
- Final state is "completed"
- No errors or crashes
