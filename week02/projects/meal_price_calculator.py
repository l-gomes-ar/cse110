# Exceeding Requirements: Tip percentage, display of Tips, \
# and the total price with and without tips were added to the normal requirements

# Prompt the user for prices, number of children/adults, tax rate, and tip percentage
meal_c = float(input("What is the price of a child's meal? "))
meal_a = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))
tip_perc = float(input("What is the tip percentage? "))

# Calculate meal's subtotal and display it
subtotal = (children * meal_c) + (adults * meal_a)
print(f"\nSubtotal: ${subtotal:.2f}")

# Compute the sales tax, the total price, tips, and the total price with tips added
sales_tax = subtotal * (tax_rate / 100)
total = subtotal + sales_tax
tips = (total * (1 + (tip_perc / 100))) - total
total_tips = total + tips

# Display the sales tax, tips, and total with tips added
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Tips: ${tips:.2f}")
print(f"Total: ${total_tips:.2f}")
print(f"Total without tips: ${total:.2f}")

# Ask the user for the payment amount
payment = float(input("\nWhat is the payment amount? "))

# Compute and display the change
change = payment - total_tips
print(f"Change: ${change:.2f}")
print()