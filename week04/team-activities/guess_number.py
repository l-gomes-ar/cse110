# Import random to use randit() function
import random

# Stretch Challenges: Loop through code as long as user wants to play it
play_again = 'yes'

while play_again == 'yes':
    # Assign a random int to a variable
    magic_number = random.randint(1, 100)

    # Stretch Challenges: Create variable for the number of attempts
    attempts = 0

    # Prompt user for a guess
    guess = -1

    # While the guess is not right loop giving hints
    while guess != magic_number:
        guess = int(input('What is your guess? '))
        # Stretch challenges keep track of guesses
        attempts = attempts + 1
        if guess < magic_number:
            print('Higher')
        elif guess > magic_number:
            print('Lower')
        
    # When the guess is right, congratulate the user
    if guess == magic_number:
        print('You guessed it!')
        if attempts != 1:
            print(f'It took you {attempts} guesses.')
        else:
            print(f'It took you {attempts} guess.')
        print()

    # Stretch Challenges: Ask user if he wants to play again.
    play_again = input('Do you want to play again? (yes/no) ').lower()
    print()

print('Thank you for playing. Goodbye. \n')