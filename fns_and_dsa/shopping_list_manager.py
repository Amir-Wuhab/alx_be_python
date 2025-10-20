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
        choice_input = input("Enter your choice: ")

        try:
            choice = int(choice_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' was added to the list.")
            
        elif choice == '2':
            
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' was removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == '3':
            
            if not shopping_list:
                print("The shopping list is currently empty.")
            else:
                print("\n--- Your Shopping List ---")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
                print("------------------------")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
