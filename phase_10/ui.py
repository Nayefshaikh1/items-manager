class TerminalUI:

    def __init__(self, service):

        self.service = service

    def menu(self):

        while True:

            print("""
===== WORKFLOW MANAGER =====

1. Register
2. Login
3. Forgot Password
4. Create Item
5. List My Items
6. Filter By State
7. View History
8. Workflow Summary
9. Update Item
10. Delete Item
11. Change State
12. Logout
13. Exit
""")

            choice = input(
                "Choose option: "
            ).strip()

            try:

                if choice == "1":

                    username = input(
                        "Username: "
                    )

                    password = input(
                        "Password: "
                    )

                    role = input(
                        "Role (user/admin): "
                    )

                    if not role:
                        role = "user"

                    self.service.register(
                        username,
                        password,
                        role
                    )

                    print(
                        "Registration successful"
                    )

                elif choice == "2":

                    username = input(
                        "Username: "
                    )

                    password = input(
                        "Password: "
                    )

                    self.service.login(
                        username,
                        password
                    )

                    print(
                        "Login successful"
                    )

                elif choice == "3":

                    username = input(
                        "Username: "
                    )

                    new_password = input(
                        "New password: "
                    )

                    self.service.forgot_password(
                        username,
                        new_password
                    )

                    print(
                        "Password updated"
                    )

                elif choice == "4":

                    title = input(
                        "Title: "
                    )

                    details = input(
                        "Details: "
                    )

                    item = (
                        self.service.create_item(
                            title,
                            details
                        )
                    )

                    print(
                        f"Created item "
                        f"{item.id}"
                    )

                elif choice == "5":

                    items = (
                        self.service.list_my_items()
                    )

                    print("\n--- ITEMS ---")

                    for item in items:
                        print(item)

                elif choice == "6":

                    state = input(
                        "State: "
                    )

                    items = (
                        self.service.filter_items(
                            state
                        )
                    )

                    print(
                        "\n--- FILTERED ITEMS ---"
                    )

                    for item in items:
                        print(item)

                elif choice == "7":

                    item_id = int(
                        input("Item ID: ")
                    )

                    history = (
                        self.service.get_history(
                            item_id
                        )
                    )

                    print("\n--- HISTORY ---")

                    for row in history:

                        print(
                            f"{row['old_state']} "
                            f"→ "
                            f"{row['new_state']} "
                            f"at "
                            f"{row['changed_at']}"
                        )

                elif choice == "8":

                    summary = (
                        self.service.workflow_summary()
                    )

                    print("\n--- SUMMARY ---")

                    for row in summary:

                        print(
                            f"{row['state']} "
                            f": "
                            f"{row['total']}"
                        )

                elif choice == "9":

                    item_id = int(
                        input("Item ID: ")
                    )

                    title = input(
                        "New title: "
                    )

                    details = input(
                        "New details: "
                    )

                    self.service.update_item(
                        item_id,
                        title,
                        details
                    )

                    print("Item updated")

                elif choice == "10":

                    item_id = int(
                        input("Item ID: ")
                    )

                    self.service.delete_item(
                        item_id
                    )

                    print("Item deleted")

                elif choice == "11":

                    item_id = int(
                        input("Item ID: ")
                    )

                    print("""
Available States:
active
blocked
completed
""")

                    new_state = input(
                        "New state: "
                    )

                    self.service.transition_item(
                        item_id,
                        new_state
                    )

                    print("State updated")

                elif choice == "12":

                    self.service.logout()

                    print("Logged out")

                elif choice == "13":

                    print("Goodbye.")
                    break

                else:

                    print("Invalid option")

            except Exception as e:

                print(f"Error: {e}")