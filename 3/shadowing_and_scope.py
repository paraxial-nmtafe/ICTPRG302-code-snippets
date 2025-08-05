# statement = "Hello!"
# times_to_celebrate = 4

# def print_with_popper(statement):
#     """ 
#     Sometimes you just want to celebrate something.

#     Parameters:
#     -----------
#     statement: (str) Something worth celebrating.

#     Returns:
#     --------
#     None 
#     """
#     print(statement, "🎉" * times_to_celebrate)
    # What is statement at this point?
    # What is times_to_celebrate?

# print(statement)
# print_with_popper("Shadowing")

# statement = input("What would you like to celebrate? ")



# print("The type of the return of print_with_popper:", type(return_val))
# print("Its equivalency to None:", return_val == None)


# ============================================================================

# What about loop variables?

# counter = 0

# (for loop)

# counter = -12

# for counter in range(0,123):
#     print(counter)


# the_word = input("Please input a word: ")
# number_of_words = int(input("Please input number of repeats: "))

# for counter in range(number_of_words):
#     print(the_word)

















#====

# Sum, Minus, Multiply and Divide function

def sum(number_a, number_b):
    result = number_a + number_b
    print(result)

def minus(number_a, number_b):
    result = number_a - number_b

def multiply(number_a, number_b):
    result = number_a * number_b

def divide(number_a, number_b):
    result = number_a / number_b

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

sum(a, b)