# ============================================================================
# Strings as iterable:
print("==== Strings as iterable ============================================")
# ============================================================================
fruit = "Durian"

# The for-loop version of letter-by-letter durian
for each_character in fruit:
    print(each_character)

# The while-loop version of letter-by-letter durian
index = 0
while index < len(fruit):
    letter_in_fruit = fruit[index]
    print(letter_in_fruit)
    index += 1 # index = index + 1

# ============================================================================
# Counting things in loops, using an accumulator
print("==== Counting things in loops, using an accumulator =================")
# ============================================================================
phrase = "She sells seashells by the sea-shore"
# Here, counter is your 'accumulator', which increases only when it sees the
# letter 'e'.
counter = 0
for each_letter in phrase:
    if(each_letter == 'e'):
        counter += 1
# So this loop tells us "How many times we saw the letter e in phrase"
# And then we can use the 'len' (length) of the string to see the percentage
# of "phrase" which is the letter e
print(str(counter / len(phrase) * 100) + "%")


# ============================================================================
# String functions and slicing
print("==== String functions and slicing ===================================")
# ============================================================================
log_phrase = "[Tagging][INFO] She sells seashells by the sea-shore"
log_phrase2 = "[Tagging][FATAL] Too many tongue-twisters"

print(log_phrase.find("sea"))
# Getting a specific letter
print(log_phrase[9])
# Getting a specific slice
print(log_phrase[9:])
print(log_phrase[:13])
print(log_phrase[:-5])
print(log_phrase[9:15])

print("Lowered phrase: " + log_phrase.lower())
# Notice that the string functions *return* a new string; they don't alter the
# original.
print("Original phrase " + log_phrase)


# Here I'm chaining "lower" and "strip" on top of the input. This is the same as doing:
# prompt = input("Do you want me to do something (yes/no) ")
# prompt = prompt.lower()
# prompt = prompt.strip()
# But it's a little easier to read.  Maybe.
prompt = input("Do you want me to do something (yes/no) ").lower().strip()

# This is very rude! We can replace a user's negative answer with an affirmative one:
prompt = prompt.replace("no", "yes")
if "yes" == prompt:
    print("Did something")


# ============================================================================
# String functions you could know
# ============================================================================
test = "    Take A look at the Different CAPITALISATIONS on these letters and what our functions might do:   "

print("Split: " + str(test.split()))
print("Strip: " + test.strip())
print("Lower: " + test.lower())
print("Upper: " + test.upper())
print("Capitalize: " + test.capitalize()) # Remember: US spelling!
print("Capitalize, but we stripped FIRST: " + test.strip().capitalize()) # Remember: US spelling!
print("Title: " + test.title())
