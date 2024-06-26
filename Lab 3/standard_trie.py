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

    def insert(self, term: str) -> None:
        """
        Inserts a term into the trie.
        :param term: Term to insert in the trie.
        """
        trie_depth = self.root

        for char in term:
            if not trie_depth.children.get(char):
                # If the character is not present at the current trie depth,
                # we create a node
                trie_depth.children[char] = TrieNode()
            # Moving downwards
            trie_depth = trie_depth.children[char]

        # Making sure there is an ending None node
        trie_depth.children[None] = TrieNode()

    def remove(self, term: str) -> str:
        """
        Returns and removes a term from the trie.
        :param term: Term to remove from the trie.
        :return: The removed term, if it exists.
        """
        if not self.term_exists(term):
            return "No such term exists in the trie."
        trie_depth = self.root
        parents = []

        # Iterating down the trie.
        for char in term:
            parents.insert(0, trie_depth)
            trie_depth = trie_depth.children[char]

        trie_depth.children.pop(None)

        reference = [*term]
        # Iterating back up
        for parent in parents:
            if trie_depth.children.get(None):
                # If the term iterates back up to a pre-existing term,
                # end the function
                return term
            trie_depth = parent
            trie_depth.children.pop(reference[-1])
            reference.pop(-1)
        return term

    def term_exists(self, term: str) -> bool:
        """
        Checks if a term exists in the trie.
        :param term: Term to check in the trie.
        :return: True if the term exists in the trie, otherwise False.
        """
        trie_depth = self.root

        for char in term:
            if not trie_depth.children.get(char):
                # If the character does not exist at that depth,
                # return False
                return False
            # Moving downwards
            trie_depth = trie_depth.children[char]

        # Validate if the character is the ending
        return True if trie_depth.children.get(None) else False
