"""
File: speller_trie.py
Authors:
    Marcus Persson (m.h.o.persson@student.rug.nl),
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    A spell checker, created using a standard trie.
"""
from standard_trie import *

# Step 1: Create the dictionary
allowed_words = StandardTrie()

word = input()
while word != "!":
    allowed_words.insert(word)
    word = input()

# Step 2: Validate if words exist in a given input.
# Handle non-alphabetical characters.
splitters = [".", ",", "\'", "’", "/", "-", "\"", ":", ";", "?", "!", "(", ")",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
unknown_word_count = 0

word = input()
while word != "":
    for splitter in splitters:
        word = " ".join(word.lower().split(splitter))
    for w in word.split():
        if not allowed_words.term_exists(w):
            print(w)
            unknown_word_count += 1
    word = input()

# Step 3: Generate output.
print("There are", unknown_word_count, "unknown words.")

word = input()
print(allowed_words.remove(word))