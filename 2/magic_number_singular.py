# Note that this code lets the user guess once!
# Also the magic number is fixed; so replayability is limited once you've guessed it.
magic_number = 16

guess = input("Guess the magic number: ")

if guess == magic_number:
    print("Congratulations 🎉, you guessed the magic number")
elif guess < magic_number:
    print("You guessed a little low")
else:
    print("You guessed too high")
