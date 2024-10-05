def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_to_add = input("Add an item: ")
            shopping_list.append(item_to_add)
            print(f'Item "{item_to_add}" has been added.')

        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input("Remove an item: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f'Item "{item_to_remove}" has been removed.')
            else:
                print(f'Error: Item "{item_to_remove}" not found in the list.')

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Your shopping list contains:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
