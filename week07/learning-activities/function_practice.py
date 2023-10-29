import math

# This function computes the area of a square
def compute_area_square(side):
    area_square = compute_area_rectangle(side, side)
    return area_square

# This function computes the area of a rectangle
def compute_area_rectangle(length, width):
    area_rectangle = length * width
    return area_rectangle

# This functions computes the area of a circle
def compute_area_circle(radius):
    area_circle = math.pi * (radius ** 2)
    return area_circle

shape = ""

while shape != "quit":
    shape = input("What kind of a shape do you have (square/rectangle/circle)? ").lower()

    if shape == "square":
        # Ask user for inputs for side of a square, compute and display the area
        side_square = float(input("What is the side of the square? "))

        area_square = compute_area_square(side_square)

        print(f"Area of the square: {area_square}")

    elif shape == "rectangle":
        # Ask user for inputs for sides of a rectangle, compute and display the area
        length_rectangle = float(input("What is the length of the rectangle? "))
        width_rectangle = float(input("What is the width of the rectangle? "))

        area_rectangle = compute_area_rectangle(length_rectangle, width_rectangle)

        print(f"The area of the rectangle is: {area_rectangle}")

    elif shape == "circle":
        # Ask user for inputs for radius of a circle, compute and display the area
        radius_circle = float(input("What is the radius of the circle? "))

        area_circle = compute_area_circle(radius_circle)

        print(f"The area of the circle is: {area_circle}")

    elif shape == 'quit':
        break

    else:
        print("Shape not valid!")