"""
You are a busy chef and want to know how many customers you can serve, given 
that you have some number stove burners available, and some number of minutes 
available to serve them in.

The only thing you cook is instant noodles, each serving of which takes one 
minute to cook on a stove.

You should take user inputs for stove_count and available_minutes.

Extension 1: You are a busier chef than you thought! You need to input how 
many stoves and how many minutes you have as a file, from 11_revision_inputs/kitchen.

Extension 2: Your noodles might now take anywhere from 1 to X minutes to cook, where
"X" is a user input number.

Output a range of number of customers that you might be serving tonight.
"""

def number_of_customers(stoves, minutes):
    return stoves * minutes

try:
    stove_count = int(input("Number of stoves? "))
    minutes_available = int(input("Enter the number of minutes available for cooking? "))
    print(
        "Number of customers that can be served:", 
        number_of_customers(stove_count, minutes_available)
        )
except:
    print("Please enter valid integer(s)")
    exit(1)
