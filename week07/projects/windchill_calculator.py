# For creativity I decided to add a while loop to keep asking the user in case he gives an invalid input for unit.
# Also, I created a function for displaying the values.

# This function computes the windchill
def calculate_windchill(t, v):
    windchill = 35.74 + (0.6215 * t) - (35.75 * (v ** 0.16)) + ((0.4275 * t) * (v ** 0.16))

    return windchill

# This function calculates and displays the windchill 
# looping through wind speeds from 5 to 60 miles per hour incrementing by 5.
def display_windchill(temperature):
    wind = 5

    for display in range(0, 12):
        windchill = calculate_windchill(temperature, wind)
        print(f"At temperature {temperature}F, and wind speed {wind} mph, the windchill is: {windchill:.2f}F")
        wind += 5

# This function converts from Celsius to Fahrenheit
def convert_fahrenheit(temperature):
    temperature = (temperature * (9 / 5)) + 32
    
    return temperature

# Ask user for temperature
temperature = float(input("What is the temperature? "))

# Ask user for unit, using while loop to ensure the input is valid
unit = ""

while unit not in ("f", "c"):
    unit = input("Fahrenheit or Celsius (F/C)? ").lower()

    if unit not in ("f", "c"):
        print("The unit must be either F or C!\n")

# Call function to display windchill
if unit == "f":
    display_windchill(temperature)

# In case the unit is Celsius, convert it to Fahrenhreit and do the same thing. 
else:
    display_windchill(convert_fahrenheit(temperature))