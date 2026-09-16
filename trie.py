class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    """Trie (prefix tree): each edge is a character, is_word marks a
    complete word ending at that node.

    Use when: prefix search/autocomplete, word search on a grid,
    "longest common prefix" over many strings.
    Time: O(L) per op, L = word/prefix length. Space: O(total chars).
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def _find(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


if __name__ == "__main__":
    trie = Trie()
    trie.insert("cat")
    trie.insert("car")
    assert trie.search("cat")
    assert not trie.search("ca")
    assert trie.starts_with("ca")
    assert not trie.starts_with("dog")
    print("ok")
