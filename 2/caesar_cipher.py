# Caesar Cipher Program.
# File: caesar-cipher.py
# Author: Para O'Kelly
# Copyright: Copyright 2025, Para O'Kelly
# This code is transitional -- it is not a caesar cipher (yet), but only a program that outputs a single character's codepoint.

print("Welcome to Caesar Cipher Program.")

name = input("What is your name? ")
print("Welcome " + name + ", I hope you enjoy the encrypting and decrypting of messages!")

character = input("What letter do you wish to encode? ")
result = ord(character)

print("The Ascii number for the character is " + str(result))
