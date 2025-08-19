statement = "Hello!"
times_to_celebrate = 4

def print_with_popper(statement):
    print(statement, "🎉" * times_to_celebrate)
    # What is statement at this point?
    # What is times_to_celebrate?

print(statement)
print_with_popper("Shadowing")

statement = input("What would you like to celebrate? ")

# This is nothing to do with shadowing and scope, but we also talked about return types:
print("The type of the return of print_with_popper:", type(return_val))
print("Its equivalency to None:", return_val == None)

# How would you get print_with_popper to return a string?