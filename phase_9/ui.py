class TerminalUI:

    def __init__(self, service):

        self.service = service

    def menu(self):

        while True:

            print("\n===== WORKFLOW MANAGER =====")

            print("1. Create Item")
            print("2. List Items")
            print("3. Update Item")
            print("4. Delete Item")
            print("5. Change State")
            print("6. Filter By State")
            print("7. View History")
            print("8. Workflow Summary")
            print("9. Exit")

            choice = input(
                "\nChoose option: "
            ).strip()

            if choice == "1":
                self.create_item()

            elif choice == "2":
                self.list_items()

            elif choice == "3":
                self.update_item()

            elif choice == "4":
                self.delete_item()

            elif choice == "5":
                self.change_state()

            elif choice == "6":
                self.filter_items()

            elif choice == "7":
                self.view_history()

            elif choice == "8":
                self.show_summary()

            elif choice == "9":

                print("Goodbye.")
                break

            else:
                print("Invalid option.")

    def create_item(self):

        title = input("Title: ").strip()

        details = input("Details: ").strip()

        if not title:

            print("Title required.")
            return

        item = self.service.create_item(
            title,
            details
        )

        print(
            f"Created item {item.id}"
        )

    def list_items(self):

        items = self.service.list_items()

        print("\n--- ITEMS ---")

        if not items:

            print("No items found.")
            return

        for item in items:
            print(item)

    def update_item(self):

        try:

            item_id = int(
                input("Item ID: ")
            )

            title = input(
                "New title: "
            ).strip()

            details = input(
                "New details: "
            ).strip()

            item = self.service.update_item(
                item_id,
                title,
                details
            )

            print(
                f"Updated item {item.id}"
            )

        except Exception as e:

            print(f"Error: {e}")

    def delete_item(self):

        try:

            item_id = int(
                input("Item ID: ")
            )

            self.service.delete_item(
                item_id
            )

            print("Item deleted.")

        except Exception as e:

            print(f"Error: {e}")

    def change_state(self):

        try:

            item_id = int(
                input("Item ID: ")
            )

            print("""
Available States:
active
blocked
completed
archived
""")

            new_state = input(
                "New state: "
            ).strip()

            if not new_state:

                print("State required.")
                return

            item = (
                self.service.transition_item(
                    item_id,
                    new_state
                )
            )

            print(
                f"Item moved to "
                f"{item.state}"
            )

        except Exception as e:

            print(f"Error: {e}")

    def filter_items(self):

        state = input(
            "State: "
        ).strip()

        items = self.service.filter_items(
            state
        )

        print(
            f"\n--- {state.upper()} ITEMS ---"
        )

        if not items:

            print("No items found.")
            return

        for item in items:
            print(item)

    def view_history(self):

        try:

            item_id = int(
                input("Item ID: ")
            )

            history = (
                self.service.get_history(
                    item_id
                )
            )

            print("\n--- HISTORY ---")

            if not history:

                print("No history.")
                return

            for row in history:

                print(
                    f"{row['old_state']} "
                    f"→ "
                    f"{row['new_state']} "
                    f"at "
                    f"{row['changed_at']}"
                )

        except Exception as e:

            print(f"Error: {e}")

    def show_summary(self):

        summary = (
            self.service.workflow_summary()
        )

        print("\n--- SUMMARY ---")

        if not summary:

            print("No items.")
            return

        for state, total in summary.items():

            print(
                f"{state}: {total}"
            )