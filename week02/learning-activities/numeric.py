# Prompt the user for their age, convert it to an int
age = int(input('How old are you? '))
# Format string to add the int+1 for the age on next birthday
print (f'On your next birthday, you will be {age + 1} years old!')
print('')

# Prompt user for the number of cartons they have
cartons = int(input('How many egg cartons do you have? '))
# Each carton has 12 eggs, multiply the variable by 12 and print the number ofeggs.
print(f'You have {cartons * 12} eggs!')
print('')

# Prompt for number of cookies
cookies = int(input('How many cookies do you have? '))
# Prompt for number of people
people = int(input('How many people are there? '))
# Determine how many cookies each person gets
print(f'Each person may have {cookies / people} cookies')
print('')