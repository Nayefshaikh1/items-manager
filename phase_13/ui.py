class TerminalUI:

    def __init__(self, service):

        self.service = service

    def menu(self):

        while True:

            print("""
===== PHASE 12 =====

1. Register
2. Login
3. Create Item
4. List All Items
5. Get Item By ID
6. Filter Items By State
7. Update Item
8. Change State
9. Delete Item
10. Exit
""")

            choice = input(
                "Choose option: "
            )

            try:

                # REGISTER
                if choice == "1":

                    username = input(
                        "Username: "
                    )

                    password = input(
                        "Password: "
                    )

                    role = input(
                        "Role: "
                    )

                    self.service.register(
                        username,
                        password,
                        role
                    )

                    print(
                        "Registered"
                    )

                # LOGIN
                elif choice == "2":

                    username = input(
                        "Username: "
                    )

                    password = input(
                        "Password: "
                    )

                    token = self.service.login(
                        username,
                        password
                    )

                    print(
                        "Login success"
                    )

                    print(
                        f"Token: {token}"
                    )

                # CREATE
                elif choice == "3":

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

                    print(item)

                # LIST ALL
                elif choice == "4":

                    items = (
                        self.service.get_all_items()
                    )

                    if not items:

                        print("No items found")

                    else:

                        for item in items:

                            print(item)

                # GET BY ID
                elif choice == "5":

                    item_id = int(
                        input("Item ID: ")
                    )

                    item = (
                        self.service.get_item(
                            item_id
                        )
                    )

                    print(item)

                # FILTER
                elif choice == "6":

                    state = input(
                        "State: "
                    )

                    items = (
                        self.service.get_items_by_state(
                            state
                        )
                    )

                    if not items:

                        print(
                            "No matching items"
                        )

                    else:

                        for item in items:

                            print(item)

                # UPDATE
                elif choice == "7":

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

                    print(
                        "Updated"
                    )

                # WORKFLOW
                elif choice == "8":

                    item_id = int(
                        input("Item ID: ")
                    )

                    state = input(
                        "New state: "
                    )

                    self.service.change_state(
                        item_id,
                        state
                    )

                    print(
                        "Workflow updated"
                    )

                # DELETE
                elif choice == "9":

                    item_id = int(
                        input("Item ID: ")
                    )

                    self.service.delete_item(
                        item_id
                    )

                    print(
                        "Deleted"
                    )

                # EXIT
                elif choice == "10":

                    break

                else:

                    print(
                        "Invalid option"
                    )

            except Exception as e:

                print(f"Error: {e}")