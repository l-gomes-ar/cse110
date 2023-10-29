# Create a list for numbers to be added
numbers = []

# Create a variable for numbers
number = None

print("Enter a list of numbers, type 0 when finished.")

# Prompt user for numbers until they quit (typing 0)
while number != 0:
    number = int(input("Enter number: "))
    numbers.append(number)

# Remove 0 from list
numbers.pop()

# Create variables for sum, largest, and smallest positive
sum_numbers = 0
largest = 0

# Create for loop for assigning those variables, and summing up
for number in numbers:
    sum_numbers += number

    if number > largest:
        largest = number

# Assign largest number in list to smallest_number 
smallest_positive = largest

for number in numbers:
    if number > 0 and number < smallest_positive:
        smallest_positive = number

# Calculate average
average = sum_numbers / len(numbers)

# Display everything
print(f"The sum is: {sum_numbers}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest positive number is: {smallest_positive}")

# Sort list
numbers.sort()

# Display the sorted list
print("The sorted list is:")
for number in numbers:
    print(number)