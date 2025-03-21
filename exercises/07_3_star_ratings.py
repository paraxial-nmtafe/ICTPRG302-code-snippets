"""
You have a collection of titles.

You are manually inputing ratings (1-5) for each title -- but there's a catch:
You are putting in ratings by many different people. At the end, I want
to be able to see the minimum rating, the maximum rating, and the average
rating of any particular title.

Inputs will have a title, a comma, and then the rating for that particular input.

You will need to use a mix of string functions, dictionary functions, and list functions.

A set of example inputs, line-by-line, might be like this:
```
Humans and Rats,1
Humans and Rats,5
Serpents and Strangers,3
Hunted by the Swamp,5
Hunted by the Swamp,2
Hunted by the Swamp,4
Humans and Rats,5
```

I would expect your output to read something like this (title order does not matter):
```
'Humans and Rats' had a minimum score of 1, a maximum score of 5, and averaged 3.6666666666666665.
'Serpents and Strangers' had a minimum score of 3, a maximum score of 3, and averaged 3.
'Hunted by the Swamp' had a minimum score of 2, a maximum score of 5, and averaged 3.6666666666666665.
```

Extension!
(You'll need to do a little research about rounding)
Those averages look a bit ugly, please instead output them to 2 decimal places, eg:
'Hunted by the Swamp' had a minimum score of 2, a maximum score of 5, and averaged 3.67.

Extension 2:
See how you might factor this into functions to improve readability.
"""

ratings = {}

while True:
    raw_input = input("Title and rating: ")
    if raw_input == "":
        break

    # Here, get your title and rating
    # Do some data checking -- you want to make sure your rating is a number, after all:

# Once you're done, you'll need to go through your list of ratings and output the format:
for title, rating_list in ratings.items():
    pass # Replace this line


