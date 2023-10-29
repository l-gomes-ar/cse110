# Import math for pi 
import math

# Calculate area of a square: Area square: length squared L **2

# Prompt the user for side of square
length_square = float(input("What is the length of a side of the square in cm? "))

# Calculate area in cm
area_square = length_square ** 2
print(f"The area of the square is: {area_square}cm\u00b2")

# Calculate area in m
area_square = area_square / 10000
print(f"The area of the square in m\u00b2 is: {area_square}m\u00b2")

# Calculate area of a rectangle both in cm and m
length_rectangle = float(input("\nWhat is the length of the rectangle in cm? "))
width_rectangle = float(input("What is the width of the rectangle in cm? "))

area_rectangle = length_rectangle * width_rectangle
print(f"The area of the rectangle is: {area_rectangle}cm\u00b2")
print(f"The aera of the rectangle is: {area_rectangle / 10000}m\u00b2")

# Area circle:
radius = float(input("\nWhat is the radius of the circle in cm? "))

area_circle = math.pi * (radius ** 2)
print(f"The area of the circle is: {area_circle:.0f}cm\u00b2")
print(f"The area of the circle is: {area_circle / 10000}m\u00b2")

"""
Prompt the user for a single length value, 
then compute and display the areas of a square with that length of side, a circle with that radius, 
and then the volumes of a cube with that side and a sphere with that radius, all from the same value from the user.
"""

# Prompt user
length = float(input("\nLength: "))

# Area Square
area_square = length ** 2
print(f"Area square with that number: {area_square}")

# Area circle
area_circle = math.pi * (length ** 2)
print(f"Area circle with that number: {area_circle:.0f}")

# Volume Cube
volume_cube = length ** 3
print(f"Volume of a cube with that number: {volume_cube}")

# Volume of a sphere
volume_sphere = ((4 / 3) * math.pi) * (length ** 3)
print(f"Volume of a sphere with that number as radius: {volume_sphere}")