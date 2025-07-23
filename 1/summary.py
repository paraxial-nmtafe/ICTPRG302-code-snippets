# Print statements make your program "output" text to the shell (standard out)
print("Mary had a little lamb")

# Input statements capture some user input string
input("Please enter a word: ")

# But are useless without variable assignment:
name = input("What is your name? ")

# This print statement includes string concatenation (con - cat - en - ation : sticking things together)
print("Hello " + name)

# Python has a number of data types "under the hood".
# Strings for "text"
# Integer for integers (whole, counting numbers, including negative numbers, to a limit)
# Float for "floating point numbers" (most numbers with a decimal point, but not all of them)
# Boolean for "True or False" data.

# You can check the datatype of any variable you like using a function called `type`
type_a = type("Some string!")
print(type_a)

type_b = type(1.23)
print(type_b)

# Type conversion:
# Python allows you to attempt to convert between types with a few different methods:
# Try some of the following code to see how it works:
# HINT: You might need to either use `print`, or run these lines from your REPL.
str(1)
float("1.23")
int(12)

ord("a")