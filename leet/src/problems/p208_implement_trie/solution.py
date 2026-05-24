class Node:
    def __init__(self):
        self.children = dict()
        self.word_end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for l in word:
            if not l in node.children:
                node.children[l] = Node()
            node = node.children[l]

        node.word_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for l in word:
            if l in node.children:
               node = node.children[l]
            else:
                return False

        return node.word_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for l in prefix:
            if l in node.children:
                node = node.children[l]
            else:
                return False

        return True
