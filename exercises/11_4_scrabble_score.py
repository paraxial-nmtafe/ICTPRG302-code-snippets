"""
For any user input, separate what is provided into words.
Return each word's scrabble score.

(You can use 11_revision_inputs/scrabble_scores to get the letter values.)

Question:
How would you check that the user inputs are real words, and not
maximum scoring, but invalid 'words', like 'zxzxzxzxz'?
"""

score_values = {}
collins_scrabble_words = []

with open("./11_revision_inputs/collins_scrabble_words.txt") as words:
    for line in words:
        collins_scrabble_words.append(line.strip().lower())

if(len(collins_scrabble_words) < 1):
    print("Valid word list failed to load")
    exit(1)

with open("./11_revision_inputs/scrabble_scores", "r") as input_file:
    for line in input_file:
        try:
            (letter, value) = line.split(",")
            score_values[letter] = int(value)
        except:
            print("Input file is invalid, should contain csv of scores")
            exit(1)

user_input = input("Please enter a scrabble word! ")
user_input = user_input.strip().lower()

def scrabble_score(user_input):
    score = 0
    for letter in user_input:
        score += score_values.get(letter, 0)
    return score

if user_input in collins_scrabble_words:
    print(user_input.capitalize(), scrabble_score(user_input))
else:
    print("Your word wasn't included in the scrabble dictionary")
