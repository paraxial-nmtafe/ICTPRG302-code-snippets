"""
Write a looping function that counts the length of a string.
(This is practice, please don't just use "len", even if that is the better way.)

For any given string, please output both it, and the length of it.
Eg, for input "Python", output "python: 6"

Extension 1:
Now you have a file of words (see 11_revision_inputs/words).  Write a new file,
"word_lengths", which contains all of the inputs from "words" but ordered from
shortest to longest, in the same format as before.

Extension 2:
The requirements have changed! You now have a new input (11_revision_inputs/sentences)
which contains entire sentences!

Please get the longest AND the shortest word from EACH LINE and use that as your
word list for the above.  Don't include duplicates in the final list.

Exclude words that are only one letter long.

Extension 3:
Do some research about regular expressions and ensure that your words from above don't
have any trailing punctuation.
"""

def word_length(word):
    count = 0
    for _ in word:
        count += 1
    return count

def print_word(word, length=None):
    return word + ": " + str(length or word_length(word)) + "\n"

# Extension 1
with open("11_revision_inputs/words", "r") as inputs:
    with open("./word_lengths", "w") as outputs:
        word_lengths = {}
        for word in inputs:
            word_lengths[word.strip()] = word_length(word.strip())

        for pair in sorted([(v, k) for (k,v) in word_lengths.items()]):
            outputs.write(print_word(pair[1], pair[0]))


# Extension 2
with open("11_revision_inputs/sentences", "r") as inputs:
    with open("./word_sentence_lengths", "w") as outputs:
        word_lengths = {}
        for line in inputs:
            print(line)
            line_words = []
            for word in line.split():
                length = word_length(word)
                print(word, length)
                if length < 2:
                    continue
                line_words.append((length, word))
            line_words.sort()

            print(line_words)
            word_lengths[line_words[0][1]] = line_words[0][0]
            word_lengths[line_words[-1][1]] = line_words[-1][0]

        print(word_lengths)
        for pair in sorted([(v, k) for (k,v) in word_lengths.items()]):
            outputs.write(print_word(pair[1], pair[0]))