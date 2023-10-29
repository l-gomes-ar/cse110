# Create list with menu options
menu = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

# Create list to store the names of the items
items = []

# Create variable for the action
action = ""

# Display introductory message
print("\nWelcome to the Shopping Cart Program!")

# Create menu system that repeats until user quits
while True:
    print("\nPlease select one of the following:")
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]}")

    action = input("Please enter an action: ")

    #  Option 1: Add the name of the item to the list
    if action == "1":
        item = input("What item would you like to add? ")
        items.append(item)

        print(f"'{item}' has been added to the cart.")

    # Option 2: Display the names of the items in the list
    elif action == "2":
        print("The contents of the shopping cart are:")
        for item in items:
            print(item)
        
        print()
    
    # Option 5: Display goodbye message and break out of loop
    elif action == "5":
        print("Thank you. Goodbye.\n")
        break

    # Invalid Option: Display error message
    else:
        print("Invalid action! Please, choose from one of the actions (1-2)!")