class TrieNode:
    """
    Trie node for prefix-based search.
    Uses a Python dict only inside the trie node to map characters to children.
    """

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Simple Trie for node-name lookup by prefix.
    Average-case insert/search is O(L), where L is the length of the word/prefix.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in str(word):
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in str(word):
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in str(prefix):
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def words_with_prefix(self, prefix):
        current = self.root
        for char in str(prefix):
            if char not in current.children:
                return []
            current = current.children[char]

        results = []
        self._collect_words(current, str(prefix), results)
        return results

    def _collect_words(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)

        for char in sorted(node.children.keys()):
            self._collect_words(node.children[char], prefix + char, results)
