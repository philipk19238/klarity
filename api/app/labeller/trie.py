from collections import defaultdict

class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_keys = set()

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert_constant(self, constant): 
        key = constant.KEY
        data = constant.DATA
        for word in data:
            end_node = self.insert_word(word)
            end_node.end_keys.add(key)

    def insert_word(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        return node
    
    def search_sentence(self, sentence):
        pairs = set()
        for word in sentence:
            pairs = pairs | self.search_word(word)
        return pairs

    def search_word(self, word):
        node = self.root
        pairs = set()
        for char in word:
            node = node.children.get(char)
            if node is None:
                return pairs
            elif node.end_keys:
                curr_pair = {(key, word) for key in node.end_keys}
                pairs = pairs | curr_pair
        return pairs
