counted_words= {}

# With thanks to Kyle S for this file handling:
with open("./text_files/romeojuliet.txt", "r") as filehandler:
    for line in filehandler:
        words = line.lower().split()
        for word in words:
            counted_words[word] = counted_words.get(word, 0) + 1

frequency_list = (sorted([
    (frequency, word)
    for (word, frequency) in counted_words.items()
]))

frequency_list.reverse()

for (frequency, word) in frequency_list[0:10]:
    print(word + ": " + str(frequency))
