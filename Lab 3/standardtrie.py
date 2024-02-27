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

    def insert_word(self, word: str) -> None:
        trie_depth = self.root

        for char in word:
            if trie_depth.children.get(char) is None:
                # If the character is not present at the current trie depth, we create a node.
                trie_depth.children[char] = TrieNode()
            # Moving downwards
            trie_depth = trie_depth.children[char]

        # Making sure there is an ending None node
        trie_depth.children[None] = TrieNode()

    def word_exists(self, word: str) -> bool:
        """
        Inserts a word into the trie.
        :param P: Word to insert in the trie.
        """
        trie_depth = self.root

        for char in word:
            if trie_depth.children.get(char) is None:
                # If the character does not exist at that depth, return False
                return False
            # Moving downwards
            trie_depth = trie_depth.children[char]

        # Validate if the character is the ending.
        return True if trie_depth.children.get(None) else False
