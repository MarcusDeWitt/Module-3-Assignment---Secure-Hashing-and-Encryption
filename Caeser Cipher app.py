"""
This app will demonstrate a simple Caeser Cipher to encrypt and decrypt messages 
input from the user. 
"""

FIRST_CHAR_CODE = ord("A") #ASCII code for 'A'
LAST_CHAR_CODE = ord("Z") #ASCII code for 'Z'
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1 

def caesar_shift(message, shift):
    #Empty string to hold the encrypted message
    result = ""

    #Go through each letter in the message.
    for char in message.upper():
        if char.isalpha(): #Check if the character is a letter.
        #Convert to ASCII code
            char_code = ord(char)
            new_char_code = char_code + shift
            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char #If it's not a letter, just add it to the result.

    print(result)

user_message = input("Enter a message to encrypt: ")
user_shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
caesar_shift(user_message, user_shift)