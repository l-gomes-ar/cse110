# Write three functions:

# display_regular—Receives a string and prints it out, exactly as received.
def display_regular(string):
    print(string)

# display_uppercase—Receives a string, converts it to upper case, and then prints it out.
def display_uppercase(string):
    string = string.upper()
    print(string)

# display_lowercase—Receives a string, converts it to lower case, and then prints it out.
def display_lowercase(string):
    string = string.lower()
    print(string)

# Ask user for a sentence. pass it to each of the three funcions
message = input("What is your message? ")

display_regular(message)
display_uppercase(message)
display_lowercase(message)