# Load dataset
with open("life-expectancy.csv") as file:

    # Skip the first line
    next(file)

    # Declare variables for highest and lowest value for life expectancy
    highest = 0
    lowest = 999

    # Iterate through data line by line
    for line in file:

        # Clean lines and split them into parts
        clean_line = line.strip()
        parts = clean_line.split(",")

        # Set variables
        life_expectancy = float(parts[3])

        # Find the highest value for life expectancy
        if life_expectancy > highest:
            highest = life_expectancy

        # Find the lowest value for life expectancy
        if  life_expectancy < lowest:
            lowest = life_expectancy
    
    # Display values
    print(f"The lowest value for life expectancy is: {lowest}")
    print(f"The highest value for life expectancy is: {highest}")       