# Introduction
print('\nIn this adventure game set you are a survivor in a world ravaged by a deadly virus')
print('that turned most of the population into zombies.')
print('You are on a mission to find a cure for the virus and save humanity.')
print('You get to the laboratory where the cure is said to be located.')
print('However, the entrance is blocked by two heavy steel doors')

first_answer = ''

# First scenario
print('\nYou notice two items lying on the ground nearby:')
first_answer = input('a CROWBAR and a HACKSAW.\nWhich one do you want to pick up? ').lower()

while True:
    # Options if crowbar is chosen
    if first_answer == 'crowbar':
        print('\nYou use the crowbar to pry open the doors.')
        print('However, the noise attracts a horde of zombies, and you must quickly find a way to escape.\n')
        break
    
    # Options if hacksaw is chosen
    elif first_answer == 'hacksaw':
        print('\nYou use the hacksaw to cut through the doors.')
        print('The process takes longer but is much quieter, and you are able to enter the laboratory undetected.\n')
        break

    else:
        while first_answer not in ('crowbar', 'hacksaw'):
            print('\nInput not valid!')
            print('\nYou notice two items lying on the ground nearby:')
            first_answer = input('a CROWBAR and a HACKSAW.\nWhich one do you want to pick up? ').lower()
