""""Generate Random Password uasing random module
First user enter number (Lenght of password) of characters to generate random password
=========================================================================================
In character string store capi letters, small lettes, numbers and symbols.
initialize empty string to store password.
check the length of password enter by user.
if mathc lenght then generate random password.
if not mathc the lenth of password then print password length should be 6 characters.
"""

import random

def generate_password(length):
    # Define the characters that can be used in the password
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$&'
    
    # Initialize an empty string to store the password
    password = ''
    
     # Check if the length of the password is valid
    if length < 6:
        print("*"*60)
        print("Password length should be at least 6 characters.")
        print("*"*60)
        return
    
    # Generate a random character from the characters string and append it to the password
    for i in range(length):
        password += random.choice(characters)
    print("*"*60)
    print(f"Here is your PassWord ::= {password}")
    print("*"*60)
    
print("*"*60)
length = int(input("Enter the Lenght of Password :: "))
generate_password(length)


