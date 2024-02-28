"""
File: standard_trie.py
Authors:
    Marcus Persson (m.h.o.persson@student.rug.nl),
    Marinus van den Ende (m.van.den.ende.1@student.rug.nl)

Description:
    A custom class for standard tries.
"""


class TrieNode:
    """
    Represents a standard trie node.
    """

    def __init__(self):
        self.children: dict[str | None, TrieNode] = dict()


class StandardTrie:
    """
    Represents a standard trie.
    """

    def __init__(self):
        self.root = TrieNode()

    def _no_word_exists(self) -> str:
        return "No such word exists in the trie."

    def insert(self, word: str) -> None:
        """
        Inserts a term into the trie.
        :param word: Term to insert in the trie.
        """
        trie_depth = self.root

        for char in word:
            if trie_depth.children.get(char) is None:
                # If the character is not present at the current trie depth,
                # we create a node
                trie_depth.children[char] = TrieNode()
            # Moving downwards
            trie_depth = trie_depth.children[char]

        # Making sure there is an ending None node
        trie_depth.children[None] = TrieNode()

    def remove_term(self, word: str) -> str:
        """
        Returns and removes a term from the trie.
        :param word: Term to remove from the trie.
        :return: The removed term, if it exists.
        """
        trie_depth = self.root
        parents = []

        # Iterating down the trie.
        for char in word:
            if trie_depth.children.get(char) is None:
                # If there is no such word,
                return self._no_word_exists()
            parents.insert(0, trie_depth)
            trie_depth = trie_depth.children[char]

        trie_depth.children.pop(None)

        reference = [*word]
        for parent in parents:
            if trie_depth.children.get(None):
                # If the word iterates back up to a pre-existing word,
                # end the function
                return word
            trie_depth = parent
            trie_depth.children.pop(reference[-1])
            reference.pop(-1)
        return word

    def term_exists(self, word: str) -> bool:
        """
        Checks if a term exists in the trie.
        :param word: Term to check in the trie.
        :return: True if the term exists in the trie, otherwise False.
        """
        trie_depth = self.root

        for char in word:
            if trie_depth.children.get(char) is None:
                # If the character does not exist at that depth,
                # return False
                return False
            # Moving downwards
            trie_depth = trie_depth.children[char]

        # Validate if the character is the ending
        return True if trie_depth.children.get(None) else False
