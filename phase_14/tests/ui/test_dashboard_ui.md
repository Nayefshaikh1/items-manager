# UI Test — Dashboard Page

## File Under Test
`web/views/dashboard.html` + `web/js/pages/dashboard.js`

---

## Test 1 — Page Load (Authenticated)

**Steps:**
1. Login successfully
2. Navigate to `dashboard.html`

**Expected:**
- Sidebar is visible with links: Dashboard, Create Item, Login
- Dashboard link is highlighted as active
- Topbar shows "Workflow Dashboard" title
- Logout button is visible in the topbar
- Summary cards show counts (Total, Draft, Active, Blocked, Completed)
- Filter bar with search input, state dropdown, and Refresh button is visible
- Items are loaded and displayed in a card grid
- Each card shows title, details, workflow badge, and "View Details" button

---

## Test 2 — Page Load (Unauthenticated)

**Steps:**
1. Clear localStorage (remove token)
2. Navigate to `dashboard.html`

**Expected:**
- User is redirected to `login.html`
- Dashboard content is never shown

---

## Test 3 — Items Display Correctly

**Steps:**
1. Create several items via the API or Create page
2. Open the dashboard

**Expected:**
- All items appear as cards in the grid
- Each card shows the item title
- Each card shows the item details text
- Each card shows a colored badge matching the item state
  - Draft = gray
  - Active = blue
  - Blocked = red
  - Completed = green
- Each card has a "View Details" button linking to `item.html?id=<id>`

---

## Test 4 — Empty State

**Steps:**
1. Delete all items (or use a fresh database)
2. Open the dashboard

**Expected:**
- The items grid is empty
- "No Items Found" empty state message is visible
- Summary counts all show 0

---

## Test 5 — Summary Card Counts

**Steps:**
1. Create items in different states (e.g., 2 draft, 3 active, 1 blocked, 1 completed)
2. Open the dashboard

**Expected:**
- Total card shows the correct total count of visible items
- Draft card shows the correct count
- Active card shows the correct count
- Blocked card shows the correct count
- Completed card shows the correct count
- Counts update when filters change

---

## Test 6 — Filter by State

**Steps:**
1. Open dashboard with items in multiple states
2. Select "Active" from the state dropdown

**Expected:**
- Only items with state "active" are shown
- Summary counts update to reflect filtered items
- Other state items are hidden
- Selecting "All States" shows all items again

---

## Test 7 — Search by Title

**Steps:**
1. Have multiple items with different titles
2. Type part of a title into the search input

**Expected:**
- Items matching the search text (in title or details) are shown
- Non-matching items are hidden
- Search is case-insensitive
- Clearing the search shows all items again
- Search works together with the state filter

---

## Test 8 — Pagination

**Steps:**
1. Create more than 6 items (LIMIT is 6)
2. Open the dashboard

**Expected:**
- Only 6 items appear on page 1
- "Page 1" text is visible
- "Prev" button is disabled on page 1
- "Next" button is enabled
- Click "Next": page 2 loads with remaining items
- "Prev" button becomes enabled on page 2
- If fewer than 6 items on current page, "Next" is disabled

---

## Test 9 — Refresh Button

**Steps:**
1. Open the dashboard
2. Create a new item via another tab or the API
3. Click the "Refresh" button

**Expected:**
- Items list reloads from the API
- The new item appears in the list
- Summary counts update

---

## Test 10 — Logout

**Steps:**
1. Open the dashboard
2. Click the "Logout" button

**Expected:**
- Success toast "Logged out" appears
- After ~500ms, user is redirected to `login.html`
- Token is removed from localStorage
- Navigating back to dashboard redirects to login

---

## Test 11 — View Details Navigation

**Steps:**
1. Open the dashboard with items
2. Click "View Details" on any item card

**Expected:**
- Browser navigates to `item.html?id=<item_id>`
- The correct item's details are shown

---

## Test 12 — API Error Handling

**Steps:**
1. Stop the backend server
2. Open or refresh the dashboard

**Expected:**
- An error message "Dashboard failed to load" or "Cannot connect to backend" appears
- The page does not crash or show a blank screen
