"""
File: speller_trie.py
Authors:
    Marcus Persson (m.h.o.persson@student.rug.nl),
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    A spell checker, created using a standard trie.
"""
from standardtrie import *

# Step 1: Create the dictionary
allowed_words = StandardTrie()

word = input()
while word != "!":
    allowed_words.insert_word(word)
    word = input()

# Step 2: Validate if words exist in a given input.
# Handle non-alpha characters.
splitters = [".", ",", "\'", "’", "/", "-", "\"", ":", ";", "?", "!", "(", ")"]
unknown_word_count = 0

word = input()
while word != "":
    for splitter in splitters:
        word = " ".join(word.lower().split(splitter))
    for w in word.split():
        if not allowed_words.word_exists(w):
            print(w)
            unknown_word_count += 1
    word = input()

# Step 3: Generate output.
print("There are", unknown_word_count, "unknown words.")
