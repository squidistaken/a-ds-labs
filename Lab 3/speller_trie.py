"""
File: speller_trie.py
Authors:
    Marcus Persson (m.h.o.persson@student.rug.nl),
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    A spell checker, created using a standard trie.
"""

# Step 1: read in the dictionary
allowed_words = []
word = input()
while word != "!":
    allowed_words.append(word)
    word = input()


# Step 2: check words
class TrieNode:
    def __init__(self):
        self.children: dict[str | None, TrieNode] = dict()


word = input()
unknown_word_count = 0

# Step 3: Generate output
print("There are", unknown_word_count, "unknown words.")
