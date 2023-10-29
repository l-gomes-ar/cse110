# Have a secret word stored
secret_word = 'Python'

# Print an introductory message
print('Welcome to the word guessing game!')
print()

# Prompt the user for a guess
guess = input('What is your guess? ').lower()

# Create a variable for the number of attempts to be used both inside and outside loops
attempts = 0

# Create a loop to keep prompting for a guess if the user did not guess it right
while guess != secret_word.lower():
    # Print a message stating that the guess was not correct
    print('Your guess was not correct.')

    # Add to the number of attempts
    attempts = attempts + 1

    # Prompt the user for another guess
    guess = input('What is your guess? ').lower()

# Check if the guess is correct, print a congratulatory message
if guess == secret_word.lower():
    # As the right guess is still a guess, add to the attempt
    attempts = attempts + 1
    print('Congratulations! you guessed it!')

    # Check if it took the user only 1 attempt
    if attempts == 1:
        print('It took you 1 guess.')

    # Print the number of attempts
    else:
        print(f'It took you {attempts} guesses.')
        
print()