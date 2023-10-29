# Prompt the user for two integers
num_1 = int(input('What is the first number: '))
num_2 = int(input('What is the second number: '))

# Write three separate if statements:
 
# If the first number is greater than the second, print "The first number is greater". 
# Otherwise, print "The first number is not greater".
if num_1 > num_2:
    print('The first number is greater')
else:
    print('The first number is not greater')

# If the two numbers are equal print "The numbers are equal". 
# Otherwise, print "The numbers are not equal".
if num_1 == num_2:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

# If the second number is greater than the first, print "The second number is greater". 
# Otherwise, print "The second number is not greater".
if num_1 < num_2:
    print('The second number is greater')
else:
    print('The second number is not greater')
print()

# Prompt the user for their favourite animal
animal = input('What is your favourite animal? ')
# Check if we have the same favourite animal
if animal.lower() == 'lion':
    print('That is my favourite animal too!')
else:
    print('That one is not my favourite.')