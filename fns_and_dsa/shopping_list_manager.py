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
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            # Add an item: solicit input and append if non-empty
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                # Handle the case of empty input
                print("No item entered. Nothing was added.")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            # Remove an item: solicit input and remove if present
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                # Inform the user if the item was not found
                print(f"'{item}' not found in your shopping list.")
            pass
        elif choice == '3':
            # Display the shopping list
            # Display the current list: show numbered items or an empty message
            if shopping_list:
                print("Your shopping list:")
                for index, entry in enumerate(shopping_list, start=1):
                    print(f"{index}. {entry}")
            else:
                print("Your shopping list is currently empty.")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()