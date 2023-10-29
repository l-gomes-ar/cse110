# Prompt user for positive number
positive_number = int(input('Please type a positive number: '))

# Ensure the number is positive, if not, loop until the user prompts a positive number 
while positive_number < 0:
    print('Sorry, that is not a positive number. Please try again.')
    positive_number = int(input('Please type a positive number: '))

# Print the positive number
print(f'The number is: {positive_number}\n')

# Kid is asking for candy
candy = '' # I do not need to ask first, as the question is going to be the same as it is in the loop

# Keep asking until the answer is no
while candy != 'yes':
    candy = input('May I have a piece of candy? ').lower()

print('Thank you.\n')