# This is an example of a recursive function -- that is, a function that calls 
# itself.  
# By nature, recursive functions must have some escape path (see the return 1,
# below) or they will keep running forever.

def factorial(level):
    if(level <= 1):
        return 1
    return level * factorial(level - 1)

print(factorial(5))