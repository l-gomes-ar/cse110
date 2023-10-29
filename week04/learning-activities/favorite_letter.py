# Create a string variable to hold the word 'Commitment'
word = 'Game Over'
favorite_letter = input('What is your favorite letter? ').lower()

# Write code that loops through the word letter by letter.
for letter in word:
    if letter.lower() == favorite_letter:
        print('_', end='')
    else:
        print(letter.lower(), end='')
        
print()