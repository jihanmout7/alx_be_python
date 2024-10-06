def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()

        # Validate user input for numeric choice
        while True:
            choice = input("Enter your choice (1-4): ")
            try:
                choice = int(choice)
                if 1 <= choice <= 4:
                    break  # Valid choice, break out of validation loop
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid choice. Please enter a number.")

        if choice == 1:
            # Validate input for adding item
            while True:
                new_item = input("Enter item name: ")
                if new_item.strip():  # Check if item name is not empty
                    shopping_list.append(new_item)
                    print(f"{new_item} added to the list.")
                    break  # Valid item name, break out of validation loop
                else:
                    print("Please enter a valid item name.")

        elif choice == 2:
            # Prompt for and remove an item
            remove_item = input("Enter item name to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} removed from the list.")
            else:
                print(f"{remove_item} not found in the list.")

        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(item)
            else:
                print("Your shopping list is currently empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()