import random

# Create a list of words
words = ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon',
'cat', 'dog', 'egg', 'fly', 'fun', 'hat', 'ice', 'jam', 'leg', 'net', 'oak', 'pig', 'sun', 'toy',
'arch', 'cake', 'dusk', 'echo', 'girl', 'hope', 'jazz', 'kite', 'lion', 'mood', 'nest', 'book']

secret_word = random.choice(words)

# Print an introductory message
print('Welcome to the word guessing game!\n')

# Create instructions for the user to understand how to play the game
print('HOW TO PLAY:\n')
print('You will receive a HINT showing how many letters there is in the secret word.')
print('Example: _ _ _ _ (4 letters)')
print('Type your guess when prompted. Your guess should be the same number of letters as the secret word.\n')
print('Your HINT will then be updated with the following information:')
print('An underscore (_) indicates that the letter is not present in the secret word.')
print('A lowercase letter (a) indicates that the letter is present somewhere in the secret word, but not at that position.')
print('An uppercase letter (A) indicates that the letter is present at that exact spot in the secret word.\n')
print('Good luck!\n')

# Print hint
print("Your hint is: ", end="")
for letter in secret_word:
    print("_", end= " ")

print()

# Declare all variables needed
guess = ""
i = 0
attempts = 0

while guess != secret_word:
    guess = input("What is your guess? ").lower()
    attempts += 1
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        print()
    
    if len(guess) == len(secret_word):
        # Only print the hint if the guess is not correct
        if guess != secret_word:
            # For each letter in the secret word go through this:
            print("Your hint is: ", end= "")
            for letter in secret_word:
                # Is the letter in the word at all?
                if guess[i] in secret_word:
                    # Is it at the exact same place?
                    if guess[i] == secret_word[i]: 
                        print(guess[i].upper(), end= " ")
                        i += 1

                    # Is it in the word but not at the same place
                    elif guess[i] != secret_word[i]: 
                        print(guess[i].lower(), end= " ")
                        i += 1
                
                # The letter is not in the word
                else: 
                    print("_", end= " ")
                    i += 1

            # Reset variable
            i = 0 
            print() 

print("Congratulations! You guessed it!")

if attempts == 1:
    print('It took you 1 guess.\n') 
    
# Print the number of attempts
else:
    print(f'It took you {attempts} guesses.\n')