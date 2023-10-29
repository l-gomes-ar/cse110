# Open file with with open() as f
with open("hr_system.txt") as f:

    print()
    for line in f:
        
        # Strip and splt line into parts
        clean_line = line.strip()
        parts = clean_line.split(" ")

        # Assess and save specific parts to variables
        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])

        # Calculate paycheck
        pay_amount = salary / 24

        # Generate bonus for engineers
        if title.lower() == "engineer":
            pay_amount += 1000

        # Display all info
        print(f"{name} (ID: {id_number}), {title} - ${pay_amount:,.2f}")

    print()
      