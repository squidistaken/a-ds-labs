"""
File: speller.py
Contributors:
    Marcus Persson (m.h.o.persson@student.rug.nl),
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    A spell checker. Modified by Marcus Persson and Marinus van den Ende.
"""


# Step 1: read in the dictionary
allowed_words = []
word = input()
while word != "!":
    allowed_words.append(word)
    word = input()

splitters = [".", ",", "\'", "’", "/", "-", "\"", ":", ";", "?", "!", "(", ")"]

# Step 2: check words
word = input()
unknown_word_count = 0
while word != "":
    for splitter in splitters:
        word = " ".join(word.lower().split(splitter))
    for w in word.split():
        if w not in allowed_words:
            print(w)
            unknown_word_count += 1
    word = input()

# Step 3: Generate output
print("There are", unknown_word_count, "unknown words.")
