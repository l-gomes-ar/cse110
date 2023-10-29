# Prompt the user for prices, number of children/adults, and tax rate
print()
meal_c = float(input("What is the price of a child's meal? "))
meal_a = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))
print()

# Calculate meal's subtotal and display it
subtotal = (children * meal_c) + (adults * meal_a)
print(f"Subtotal: ${subtotal:.2f}")
print()