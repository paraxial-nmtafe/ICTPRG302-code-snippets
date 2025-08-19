# Define a function!

# This simple function has no parameters, and so, takes no arguments.
def some_name():
    print("hello")

# Despite taking no arguments, you still need to give it brackets, or
# Python won't know that you want it to run the function!
some_name()


# This function takes 2 parameters, which can be used like "local
# variables" inside the function (but not outside!)
# This function additionally `returns` a value!
def addition(number_a, number_b):
    return number_a + number_b

# Here's where we pass the arguments to this function...
sum = addition(1, 5)

# The program doesn't put anything into "the output" until we ask it to.
print(sum)

# print(sum == None)
# print(type(sum))

# Here's an exercise:
# Please write a function
# Called "repeat_words"
# With 2 parameters, the_word, number_of_repeats
#
# Calling it would look like this:
# repeat_words("hello", 5)
#
# And the output looks like:
# hello
# hello
# hello
# hello
# hello

# Solution:
user_count = int(input("Enter the number of times to display word"))
user_word = str(input("Enter the string"))

def repeat_words(word, count):
    # Look at this! The loop variable is called "_", because we
    # don't use it.  It's a convention to call a variable that
    # we have to declare but don't want to use with an underscore.
    for _ in range(count):
        print(word)

repeat_words(user_word, user_count)
