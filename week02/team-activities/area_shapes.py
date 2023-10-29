# Calculate the areas of a square, rectangle, and circle, 
# Import math for pi 
import math

# Prompt the user for lengths, width, and radius in cm, then compute and display the areas both in cm and m squared
# Square:
length_sq = float(input('What is the length of a side of the square in cm? '))
area_sq = length_sq ** 2
print(f'The area of the square in cm\u00b2 is: {area_sq:,}cm\u00b2')
print(f'The area of the square in m\u00b2 is: {area_sq / 10000:,.2f}m\u00b2')

# Rectangle:
length_rect = float(input('What is the length of the rectangle? '))
width_rect = float(input('What is the width of the rectangle? '))
area_rect = length_rect * width_rect
print(f'The area of the rectangle in cm\u00b2 is: {area_rect:,.2f}cm\u00b2')
print(f'The area of the rectangle in m\u00b2 is:{area_rect / 10000:,.2f}m\u00b2')

# Circle: 
radius = float(input('What is the radius of the circle? '))
area_cir = math.pi * (radius ** 2)
print(f'The area of the circle in cm\u00b2 is: {area_cir}cm\u00b2')
print(f'Thea area of the circle in m\u00b2 is:{area_cir / 10000:,.2f}m\u00b2')

# Stretch challenges
# Prompt user for a single length value
length = float(input('Single length value: '))

# Compute the areas of; 
# a square, circle, cube and sphere
a_sq = length ** 2
a_cir = math.pi * (length ** 2)
volume_cube = length ** 3
volume_sphere = ((4 / 3) * math.pi) * (length ** 3)

# Display results
print(f'Area of a square: {a_sq:,.2f}')
print(f'Area of a circle: {a_cir:,.2f}')
print(f'Volume of a cube: {volume_cube:,.2f}')
print(f'Volume of a sphere: {volume_sphere:,.2f}')