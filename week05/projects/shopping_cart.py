# Exceeding Requirements: Added 'capitalize()' function in the input for the items, added message for empty shopping cart,
# added an 'invalid action' message in case the user wants to prompt anything other than the numbers 1 to 5.

# Create list with menu options
menu = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

# Create list to store the names and prices of the items
items = []
prices = []

# Create variable for action
action = ""

# Display introductory message
print("\nWelcome to the Shopping Cart Program!")

# Create menu system that repeats until user quits
while True:
    print("\nPlease select one of the following:")
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]}")

    action = input("Please enter an action: ")

    #  Option 1: Add name and price of the item to the list
    if action == "1":
        item = input("What item would you like to add? ").capitalize()
        price = float(input(f"What is the price of '{item}'? "))
        items.append(item)
        prices.append(price)

        print(f"'{item}' has been added to the cart.")

    # Option 2: Display the names of the items in the list
    elif action == "2":

        if len(items) != 0:
            print("The contents of the shopping cart are:")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")
        
        else:
            print("Your shopping cart is empty.")

    # Option 3: Complete option to remove item
    elif action == "3":
        remove = int(input("Which item would you like to remove? "))

        # Convert to 0-based index
        remove -= 1

        # Check if index is valid
        if remove > -1 and remove < len(items):
            items.pop(remove)
            prices.pop(remove)

            print("Item removed.")
        
        else:
            print("Sorry, that is not a valid item number.")

    # Option 4: Compute and display the total amount     
    elif action == "4":
        total_amount = 0

        for price in prices:
            total_amount += price

        print(f"The total price of the items in the shopping cart is: ${total_amount:.2f}")

    # Option 5: Display goodbye message and break out of loop
    elif action == "5":
        print("Thank you. Goodbye.\n")
        break

    # Invalid option: Display error message
    else:
        print("Invalid action! Please, choose from one of the actions (1-5)!")