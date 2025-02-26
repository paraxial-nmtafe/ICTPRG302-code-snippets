"""
    This script will take any string of the following format:
    (d|e)(0-99)(A word to cipher)
    And output a ciphered message from there.  D stands for "decrypt" and E stands for "Encrypt".

    For example, "d 3khoor" will produce the output "hello".

    This code snippet is only one of many ways to solve this problem, and is released to help 
    facilitate learning alongside Cert IV ICTPRG302, Session 3, which described the use of
    functions.

    Please attempt the exercise yourself before looking at this code.
"""

def welcome():
    print("Welcome to the Casear cipher program")
    name = input("What is your name? ")
    print(name + ", I hope you enjoy encrypting and decrypting words.")
    return name

def character_shift(char, shift):
    # Don't bother shifting non-alphabetical characters:
    if not char.isalpha():
        return char

    return chr(ord(char) + shift)

# This function accounts for the end of the alphabet and will wrap our cipher around.
# How would you hook this into the program execution? It's not used yet.
def wrapped_character_shift(char, shift):
    if not char.isalpha():
        return char

    character_is_upper = char.isupper()
    unwrapped_shift = ord(char.lower()) + shift
    wrapped_shift = ((unwrapped_shift - ord('a')) % 26) + ord('a')
    if character_is_upper:
        return chr(wrapped_shift).upper()

    return chr(wrapped_shift)

def encrypt(raw_word, shift):
    ciphered_word = ""
    for character in raw_word:
        ciphered_word = ciphered_word + character_shift(character, shift)
    return ciphered_word

name = welcome()
raw_input = input("String to encrypt: ")
operation = raw_input[0].lower()
shift = raw_input[1:3].strip()
raw_word = raw_input[3:]

print(shift)

if not shift.isnumeric():
    print("Ensure that your 2nd and 3rd characters are numerical")
    exit(1)

try:
    shift = int(shift)
except ValueError:
    shift = 0

print("")
print(name + ", here's your output, shifted by", shift, "character(s):")
print("Original word:", raw_word)
if operation == "e":
    print("Encrypted:", encrypt(raw_word, shift))
else:
    print("Decrypted:", encrypt(raw_word, -shift))

