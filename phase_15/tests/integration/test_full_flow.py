import unittest


import unittest
from app_context import service, auth, repo
from item import Item
from db import cursor, connection

class FullFlowTest(unittest.TestCase):

    def setUp(self):
        # Clean the DB for the test
        cursor.execute("DELETE FROM workflow_history")
        cursor.execute("DELETE FROM items")
        cursor.execute("DELETE FROM users")
        connection.commit()

    def test_full_application_flow(self):
        # 1. Register
        service.register("e2e_user", "password123", "admin")
        
        # 2. Login (Get Token)
        token = service.login("e2e_user", "password123")
        self.assertIsNotNone(token)
        
        # 3. Create Item
        created_item = service.create_item("Integration Test", "Testing the full flow", "e2e_user")
        self.assertIsNotNone(created_item.id)
        self.assertEqual(created_item.state, "draft")
        
        # 4. Transition State
        updated_item = service.change_state(created_item.id, "active")
        self.assertEqual(updated_item.state, "active")
        
        # 5. Verify History
        history = service.get_history(created_item.id)
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["old_state"], "draft")
        self.assertEqual(history[0]["new_state"], "active")
        
        # 6. Check Summary
        summary = service.workflow_summary()
        self.assertEqual(summary.get("active"), 1)

if __name__ == "__main__":
    unittest.main()