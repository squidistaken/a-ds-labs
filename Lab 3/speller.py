"""
File:   speller.py

Description:
    A spell checker
"""


# Step 1: read in the dictionary
allowed_words = []
word = input()
while word != "!":
    allowed_words.append(word)
    word = input()

# Step 2: check words
word = input()
unknown_word_count = 0
while word != "":
    if word not in allowed_words:
        print(word)
        unknown_word_count += 1
    word = input()

# TODO: Replace the above while loop with a correct solution.

# Step 3: Generate output
print("There are", unknown_word_count, "unknown words.")
