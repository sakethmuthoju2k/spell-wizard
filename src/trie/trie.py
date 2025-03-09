class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True

    def search(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                return False
            else:
                node = node.children[ch]
        
        return (node.is_end == True)