# Write a program to convert from Fahrenheit to Celsius.
# Prompt user for Fahrenheit unit
fahrenheit = int(input('What is the temperature in Fahrenheit? '))

#Convert it to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Print the temperature in Celsius
print(f'The temperature in Celsius is {celsius:.1f} degrees.')