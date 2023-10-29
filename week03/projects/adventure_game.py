# To show creativity, I decided to use while loops to handle the 'else' statement problem,in case
# the user's input was not valid, I added an if statement to correct them. I also added more scenarios to the story.

# Introduction
print('\nIn this adventure game set you are a survivor in a world ravaged by a deadly virus')
print('that turned most of the population into zombies.')
print('You are on a mission to find a cure for the virus and save humanity.')
print('You get to the laboratory where the cure is said to be located.')
print('However, the entrance is blocked by two heavy steel doors')

# Declare all variables so that we can use them outside if-statements and while-loops
first_answer = ''
second_answer = ''
third_answer = ''
fourth_answer = ''
fifth_answer = ''
sixth_answer = ''
seventh_answer = ''
eigth_answer = ''

# Create messages and store them into variables to print them afterwards:

# Create 'GAME OVER' message
gameover = '-------------------\n\
   # GAME OVER #\
\n-------------------'

# Create 'neutral' ending message
neutral_end = 'You managed to escape the laboratory, but the world outside is still a dangerous and unforgiving place.\n\
Your journey has come to an end, but your struggle for survival continues.'

# Create 'bad' ending message
bad_end = 'Your hope and courage were not enough to overcome the dangers of this new world.\n\
Your quest for the cure has failed, and the world remains in darkness.'

# Create 'good' ending message
good_end = 'You have succeeded in your mission and found the cure that will save humanity.\n\
Your bravery and determination have made the difference between life and death,\n\
and the world will never forget your sacrifice.'

# Create 'invalid input' message
invalid = '\nInvalid input! Please, type one of the choices in ALL CAPS.'


# First scenario
while first_answer not in ('crowbar', 'hacksaw'):
    print('\nYou notice two items lying on the ground nearby:')
    print('a CROWBAR and a HACKSAW')
    first_answer = input('Which one do you want to pick up? ').lower()

    # In case the user does not type a valid input, display 'invalid' message
    if first_answer not in ('crowbar', 'hacksaw'):
        print(invalid)

# Options if crowbar is chosen
if first_answer == 'crowbar':
    print('\nYou use the crowbar to pry open the doors.')
    print('However, the noise attracts a horde of zombies, and you must quickly find a way to escape.')

    while second_answer not in ('bat', 'knife', 'gun'):
        print('\nYou find yourself in a narrow alley, surrounded by zombies.')
        print('You notice three items lying on the ground nearby:')
        second_answer = input('a baseball BAT, a KNIFE, and a GUN. Which one do you want to pick up? ').lower()

        if second_answer not in ('bat', 'knife', 'gun'):
            print(invalid)

    # If option 'bat' is chosen
    if second_answer == 'bat':
        print("\nYou use the baseball bat to bash the zombies' heads in.")
        print("It's a tough fight, but you manage to survive and make it to the other end of the alley.")

        while fourth_answer not in ('exit', 'storage'):
            print('\nYou find yourself in a dead-end street with two doors:')
            fourth_answer = input('One is marked "EXIT," and the other is marked "STORAGE." Which one do you want to open? ').lower()

            if fourth_answer not in ('exit', 'storage'):
                print(invalid)

        # If option 'exit' is chosen
        if fourth_answer == 'exit':
            print('\nYou go through the exit door.')
            print('You find yourself outside the laboratory and manage to escape to safety.')
            print(f'\n{neutral_end}\n{gameover}\n')

        # If option 'storage' is chosen
        else:
            print('\nYou go through the storage door.')
            print('You open it to find a group of heavily armed survivors who mistake you for a zombie and shoot you on sight.')
            print(f'\n{bad_end}\n{gameover}\n')

    # If option 'knife' is chosen
    elif second_answer == 'knife':
        print('\nYou pick up the knife, you try to stab your way through the zombies.')
        print('However, the knife breaks in the process, and you are overwhelmed and turned into a zombie.')
        print(f'\n{bad_end}\n{gameover}\n')

    # If option 'gun' is chosen
    else:
        print('\nYou pick up the gun and shoot your way through the zombies, making it to safety.')
        print('But give up on going back to finish your quest for the cure.')
        print(f'\n{neutral_end}\n{gameover}\n')

# Options if hacksaw is chosen
else:
    print('\nYou use the hacksaw to cut through the doors.')
    print('The process takes longer but is much quieter, and you are able to enter the laboratory undetected.')

    while third_answer not in ('right', 'left'):
        print('\nYou enter the laboratory and find two corridors:')
        print('One on the RIGHT and another on the LEFT.')
        third_answer = input('Which one do you want to go through? ').lower()

        if third_answer not in ('right', 'left'):
            print(invalid)

    # If option 'right' is chosen
    if third_answer == 'right':
        while fifth_answer not in ('office', 'maintenance'):
            print('\nYou go through the right corridor.')
            print('Near the end you find two rooms:')
            print('an OFFICE and a MAINTENANCE workshop')
            fifth_answer = input('Which one do want to search first? ').lower()

            if fifth_answer not in ('office', 'maintenance'):
                print(invalid)

        # If option 'office' is chosen
        if fifth_answer == 'office':
            print("\nYou open the door to the office first.")
            print("When you go inside you hear a loud alarm.")
            print("This attracts the attention of the laboratory's security team.")
            print('You are caught and executed on the spot.')
            print(f'\n{bad_end}\n{gameover}\n')

        # If option 'maintenance' is chosen
        else:
            while sixth_answer not in ('cupboard', 'exit'):
                print('\nYou open the door to the maintenance workshop.')
                print('As you go inside you notice a huge cupboard.')
                print('As well as a single door next to it with the sign “exit”')
                sixth_answer = input('Do you open the CUPBOARD or EXIT through the door? ').lower()

                if sixth_answer not in ('cupboard', 'exit'):
                    print(invalid)

            # If option 'cupboard' is chosen
            if sixth_answer == 'cupboard':
                print('\nYou open the cupboard.')
                print('By doing so, you accidently trigger a bomb prototype that explodes.')
                print('Killing you at once.')
                print(f'\n{bad_end}\n{gameover}\n')

            # If option 'exit' is chosen
            else:
                print('\nYou open the exit door, which triggers an alarm.')
                print('Your only choice now is to run away as fast as you can, in order to escape')
                print('from the staff and nearby zombies that heard the alarm.')
                print(f'\n{neutral_end}\n{gameover}\n')

    # If option 'left' is chosen
    else:
        while seventh_answer not in ('garden', 'lab'):
            print('\nYou go through the left corridor.')
            print('Near the end you find two rooms:')
            print('a GARDEN and a LAB')
            seventh_answer = input('Which one do want to search first? ').lower()

            if seventh_answer not in ('garden', 'lab'):
                print(invalid)

        # If option 'garden' is chosen
        if seventh_answer == 'garden':
            print('\nYou open the door to the garden.')
            print('As you leave you notice a lot of zombies there.')
            print('These are kept by the laboratory for experiments.')
            print('They quickly get to you and turn you into a zombie.')
            print(f'\n{bad_end}\n{gameover}\n')

        # If option 'lab' is chosen
        else:
            while eigth_answer not in ('computer', 'refrigerator', 'window'):
                print('\nYou open the door to the lab.')
                print('As soon as you are inside you notice three main things:')
                print('a COMPUTER, a small REFRIGERATOR, and a single WINDOW.')
                eigth_answer = input('Which one do you want to search? ').lower()

                if eigth_answer not in ('computer', 'refrigerator', 'window'):
                    print(invalid)

            # If option 'computer' is chosen
            if eigth_answer == 'computer':
                print('\nYou decide to look the computer.')
                print('When you try to log in you send an alarm to the laboratory staff.')
                print('They quickly get where you are and execute you on spot.')
                print(f'\n{bad_end}\n{gameover}\n')

            # If option 'refrigerator' is chosen
            elif eigth_answer == 'refrigerator':
                print('\nYou open the small refrigerator.')
                print('You discover that this is where they kept the vaccines.')
                print('You get the cure and manage to make it out of the laboratory alive.')
                print(f'\n{good_end}\n{gameover}\n')

            # If option 'window' is chosen
            else:
                print('\nYou approach the window.')
                print('A sniper that guards the lab from outside sees you.')
                print('He shoots you, killing you instantly.')
                print(f'\n{bad_end}\n{gameover}\n')