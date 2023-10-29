# Ask the user for their grade percentage
grade_percentage = float(input('What is your grade percentage? '))

# Determine the letter grade and store it in a variable
if grade_percentage >= 90:
    letter = 'A'

elif grade_percentage >= 80:
    letter = 'B'

elif grade_percentage >= 70:
    letter = 'C'

elif grade_percentage >= 60:
    letter = 'D'

else:
    letter = 'F'

# Determine the sign of the grade, and store it in a variable
if grade_percentage % 10 >= 7:
    sign = '+'

elif grade_percentage % 10 < 3:
    sign = '-'

else:
    sign = ''

# Recognise there is no A+ grade
if grade_percentage >= 93:
    sign = ''

# Recognise there is no F+, or F- grades
if grade_percentage < 60:
    sign = ''

print(f'Your letter grade is: {letter}{sign}!')

if grade_percentage >= 70:
    print('Congratulations! You passed!')

else:
    print('Unfortunately, you did not pass this class. But next time you will get it!')