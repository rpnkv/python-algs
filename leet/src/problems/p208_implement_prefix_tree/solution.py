class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False


class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = Node()
            root = root.children[c]

        root.is_word = True

    def _search_node(self, word) -> Node | None:
        root = self.root

        for c in word:
            if c in root.children:
                root = root.children[c]
            else:
                return None

        return root

    def search(self, word: str) -> bool:
        node = self._search_node(word)

        return bool(node) and node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self._search_node(prefix)

        return bool(node)
