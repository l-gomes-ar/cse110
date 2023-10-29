people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# Declare variables for the youngest person (name and age)
youngest_name = ""
youngest_age = 100

# Iterate through each line of the list
for person in people:
    # Split the list into names and ages
    person = person.split()

    # Create a variable to store the name
    name = person[0] # In this case, [0] as the name is the first part of the line
    age = int(person[1]) # In this case, [1] as the age is the second part. Cast it as int to use operators

    # Check the age, if it is youngest than the current youngest, reassign it to youngest_age
    if age < youngest_age:
        youngest_age = age

        # Also keep track of the name of the youngest person
        youngest_name = name

# Display
print(f"The youngest person is: {youngest_name}, who is {youngest_age} years old.")